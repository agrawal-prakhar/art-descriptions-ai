#!/usr/bin/env python3
"""
Example usage of the Art Descriptions AI system.
This script demonstrates how to use the ArtDescriptor class programmatically.
"""

import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.art_descriptor import ArtDescriptor


def example_single_image():
    """Example: Process a single image."""
    print("=== Example: Single Image Processing ===")
    
    # Initialize the art descriptor
    descriptor = ArtDescriptor()
    
    # Example image path (you would replace this with your actual image)
    image_path = "assets/example_artwork.jpg"
    
    # Check if the image exists
    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        print("Please add an image to the assets folder and update the path in this example.")
        return
    
    # Generate description
    result = descriptor.generate_description(image_path)
    
    if result['status'] == 'success':
        print(f"Successfully processed: {result['filename']}")
        print(f"Description: {result['description'][:200]}...")
        print(f"Tokens used: {result['tokens_used']}")
    else:
        print(f"Error: {result['error']}")


def example_bulk_processing():
    """Example: Process multiple images in bulk."""
    print("\n=== Example: Bulk Processing ===")
    
    # Initialize the art descriptor
    descriptor = ArtDescriptor()
    
    # Process all images in the assets folder
    results = descriptor.process_bulk_images()
    
    print(f"Processed {len(results)} images")
    
    # Show summary
    successful = [r for r in results if r['status'] == 'success']
    failed = [r for r in results if r['status'] == 'error']
    
    print(f"Successful: {len(successful)}")
    print(f"Failed: {len(failed)}")
    
    if failed:
        print("Failed files:")
        for result in failed:
            print(f"  - {result['filename']}: {result['error']}")


def example_custom_prompt():
    """Example: Using a custom prompt."""
    print("\n=== Example: Custom Prompt ===")
    
    # Initialize the art descriptor
    descriptor = ArtDescriptor()
    
    # Custom prompt focused on historical context
    custom_prompt = """
    You are an art historian specializing in museum accessibility. 
    Please provide a detailed description of this artwork that includes:
    
    1. The historical period and artistic movement
    2. The cultural and social context of when it was created
    3. The artist's background and significance
    4. The technical methods and materials used
    5. The artwork's impact and legacy in art history
    
    Make the description engaging and educational for museum visitors with visual impairments.
    Focus on making the historical significance and artistic value accessible through vivid descriptions.
    """
    
    # Example image path
    image_path = "assets/example_artwork.jpg"
    
    if os.path.exists(image_path):
        result = descriptor.generate_description(image_path, custom_prompt)
        
        if result['status'] == 'success':
            print(f"Custom description for: {result['filename']}")
            print(f"Description: {result['description'][:300]}...")
        else:
            print(f"Error: {result['error']}")
    else:
        print("Example image not found. Please add an image to test this feature.")


def example_csv_export():
    """Example: Export results to CSV."""
    print("\n=== Example: CSV Export ===")
    
    # Initialize the art descriptor
    descriptor = ArtDescriptor()
    
    # Process images and export to CSV
    results = descriptor.process_bulk_images()
    descriptor.export_to_csv(results)
    
    print("Results exported to CSV format for easy analysis.")


def main():
    """Run all examples."""
    print("Art Descriptions AI - Example Usage")
    print("=" * 50)
    
    try:
        # Run examples
        example_single_image()
        example_bulk_processing()
        example_custom_prompt()
        example_csv_export()
        
        print("\n" + "=" * 50)
        print("All examples completed!")
        print("\nTo use this system:")
        print("1. Add your artwork images to the 'assets' folder")
        print("2. Set your OpenAI API key in a .env file")
        print("3. Run: python main.py --bulk")
        print("4. Or use the programmatic interface as shown in these examples")
        
    except Exception as e:
        print(f"Error running examples: {e}")
        print("Make sure you have:")
        print("1. Installed all requirements: pip install -r requirements.txt")
        print("2. Set up your OpenAI API key in a .env file")
        print("3. Added some images to the assets folder")


if __name__ == "__main__":
    main() 