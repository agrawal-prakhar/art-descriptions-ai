#!/usr/bin/env python3
"""
Art Descriptions AI - Main Script
Generate accessibility-focused visual descriptions of artwork images using OpenAI API.
"""

import argparse
import sys
import os
from pathlib import Path

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.art_descriptor import ArtDescriptor
from src.config import Config


def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate accessibility-focused descriptions of artwork images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all images in assets folder
  python main.py --bulk

  # Process a single image
  python main.py --image path/to/artwork.jpg

  # Process with custom prompt
  python main.py --bulk --prompt "Describe this artwork focusing on its historical significance"

  # Export results to CSV
  python main.py --bulk --export-csv

  # Process with example images and descriptions
  python main.py --bulk --with-examples --example-images assets/example1.jpg,assets/example2.jpg --example-descriptions "Description 1","Description 2"
        """
    )
    
    parser.add_argument(
        '--image', 
        type=str, 
        help='Path to a single image file to process'
    )
    
    parser.add_argument(
        '--bulk', 
        action='store_true',
        help='Process all images in the assets folder'
    )
    
    parser.add_argument(
        '--input-dir', 
        type=str, 
        default=Config.ASSETS_DIR,
        help=f'Input directory for bulk processing (default: {Config.ASSETS_DIR})'
    )
    
    parser.add_argument(
        '--output-file', 
        type=str,
        help='Output file path for results (default: descriptions/bulk_descriptions.json)'
    )
    
    parser.add_argument(
        '--prompt', 
        type=str,
        help='Custom prompt to use instead of the default accessibility prompt'
    )
    
    parser.add_argument(
        '--export-csv', 
        action='store_true',
        help='Export results to CSV format'
    )
    
    parser.add_argument(
        '--list-images', 
        action='store_true',
        help='List all supported images in the input directory'
    )
    
    parser.add_argument(
        '--with-examples',
        action='store_true',
        help='Use example images and descriptions for better guidance'
    )
    
    parser.add_argument(
        '--example-images',
        type=str,
        help='Comma-separated list of example image paths'
    )
    
    parser.add_argument(
        '--example-descriptions',
        type=str,
        help='Comma-separated list of example descriptions (must match number of example images)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.image and not args.bulk and not args.list_images:
        parser.error("Please specify either --image, --bulk, or --list-images")
    
    # Validate example arguments
    if args.with_examples:
        if not args.example_images or not args.example_descriptions:
            parser.error("--with-examples requires both --example-images and --example-descriptions")
        
        example_images = [img.strip() for img in args.example_images.split(',')]
        example_descriptions = [desc.strip() for desc in args.example_descriptions.split(',')]
        
        if len(example_images) != len(example_descriptions):
            parser.error("Number of example images must match number of example descriptions")
    
    try:
        # Initialize art descriptor
        descriptor = ArtDescriptor()
        
        # List images if requested
        if args.list_images:
            list_supported_images(args.input_dir)
            return
        
        # Process single image
        if args.image:
            if args.with_examples:
                process_single_image_with_examples(descriptor, args.image, args.prompt, example_images, example_descriptions)
            else:
                process_single_image(descriptor, args.image, args.prompt)
            return
        
        # Process bulk images
        if args.bulk:
            if args.with_examples:
                results = process_bulk_images_with_examples(
                    descriptor, 
                    args.input_dir, 
                    args.output_file, 
                    args.prompt,
                    example_images,
                    example_descriptions
                )
            else:
                results = process_bulk_images(
                    descriptor, 
                    args.input_dir, 
                    args.output_file, 
                    args.prompt
                )
            
            # Export to CSV if requested
            if args.export_csv:
                descriptor.export_to_csv(results)
            
            return
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def list_supported_images(input_dir: str):
    """List all supported images in the input directory."""
    from pathlib import Path
    
    image_files = []
    for ext in Config.SUPPORTED_FORMATS:
        image_files.extend(Path(input_dir).glob(f"*{ext}"))
        image_files.extend(Path(input_dir).glob(f"*{ext.upper()}"))
    
    if not image_files:
        print(f"No supported image files found in {input_dir}")
        print(f"Supported formats: {', '.join(Config.SUPPORTED_FORMATS)}")
        return
    
    print(f"Found {len(image_files)} supported images in {input_dir}:")
    for image_file in sorted(image_files):
        print(f"  - {image_file.name}")


def process_single_image(descriptor: ArtDescriptor, image_path: str, custom_prompt: str = None):
    """Process a single image and display the result."""
    print(f"Processing image: {image_path}")
    
    result = descriptor.generate_description(image_path, custom_prompt)
    
    if result.get('status') == 'success':
        print("\n" + "="*50)
        print("GENERATED DESCRIPTION")
        print("="*50)
        print(f"Filename: {result['filename']}")
        print(f"Model: {result['model_used']}")
        if result.get('tokens_used'):
            print(f"Tokens used: {result['tokens_used']}")
        print("\nDescription:")
        print("-" * 30)
        print(result['description'])
        print("="*50)
        
        # Save to file
        output_file = os.path.join(
            Config.DESCRIPTIONS_DIR, 
            f"{Path(image_path).stem}_description.json"
        )
        import json
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nResult saved to: {output_file}")
        
    else:
        print(f"Error processing {image_path}: {result.get('error', 'Unknown error')}")


def process_bulk_images(descriptor: ArtDescriptor, input_dir: str, output_file: str, custom_prompt: str = None):
    """Process multiple images in bulk."""
    print(f"Starting bulk processing of images in: {input_dir}")
    if custom_prompt:
        print("Using custom prompt")
    
    results = descriptor.process_bulk_images(input_dir, output_file, custom_prompt)
    
    return results


def process_single_image_with_examples(descriptor: ArtDescriptor, image_path: str, custom_prompt: str = None, example_images: list = None, example_descriptions: list = None):
    """Process a single image with examples and display the result."""
    print(f"Processing image with examples: {image_path}")
    
    result = descriptor.generate_description_with_examples(image_path, example_images, example_descriptions, custom_prompt)
    
    if result.get('status') == 'success':
        print("\n" + "="*50)
        print("GENERATED DESCRIPTION WITH EXAMPLES")
        print("="*50)
        print(f"Filename: {result['filename']}")
        print(f"Model: {result['model_used']}")
        print(f"Examples used: {result.get('examples_used', 0)}")
        if result.get('tokens_used'):
            print(f"Tokens used: {result['tokens_used']}")
        print("\nDescription:")
        print("-" * 30)
        print(result['description'])
        print("="*50)
        
        # Save to file
        output_file = os.path.join(
            Config.DESCRIPTIONS_DIR, 
            f"{Path(image_path).stem}_description_with_examples.json"
        )
        import json
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nResult saved to: {output_file}")
        
    else:
        print(f"Error processing {image_path}: {result.get('error', 'Unknown error')}")


def process_bulk_images_with_examples(descriptor: ArtDescriptor, input_dir: str, output_file: str, custom_prompt: str = None, example_images: list = None, example_descriptions: list = None):
    """Process multiple images in bulk with examples."""
    print(f"Starting bulk processing of images in: {input_dir}")
    print(f"Using {len(example_images)} example images for guidance")
    if custom_prompt:
        print("Using custom prompt")
    
    results = descriptor.process_bulk_images_with_examples(input_dir, output_file, example_images, example_descriptions, custom_prompt)
    
    return results


if __name__ == "__main__":
    main() 