import os
import json
import base64
from pathlib import Path
from typing import List, Dict, Optional
import openai
from PIL import Image
import io
from tqdm import tqdm
import pandas as pd

from .config import Config


class ArtDescriptor:
    """Main class for generating accessibility-focused descriptions of artwork images."""
    
    def __init__(self):
        """Initialize the ArtDescriptor with OpenAI client."""
        Config.validate_config()
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
        
    def encode_image(self, image_path: str) -> str:
        """Encode image to base64 string for OpenAI API."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def get_image_info(self, image_path: str) -> Dict:
        """Get basic information about an image."""
        try:
            with Image.open(image_path) as img:
                return {
                    'filename': os.path.basename(image_path),
                    'format': img.format,
                    'size': img.size,
                    'mode': img.mode
                }
        except Exception as e:
            return {
                'filename': os.path.basename(image_path),
                'error': str(e)
            }
    
    def generate_description(self, image_path: str, custom_prompt: Optional[str] = None) -> Dict:
        """
        Generate a visual description for a single artwork image.
        
        Args:
            image_path: Path to the image file
            custom_prompt: Optional custom prompt to override the default accessibility prompt
            
        Returns:
            Dictionary containing the description and metadata
        """
        try:
            # Validate image file
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image file not found: {image_path}")
            
            # Get image info
            image_info = self.get_image_info(image_path)
            
            # Encode image
            base64_image = self.encode_image(image_path)
            
            # Use custom prompt or default accessibility prompt
            prompt = custom_prompt if custom_prompt else Config.ACCESSIBILITY_PROMPT
            
            # Make API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1000,
                temperature=0.7
            )
            
            description = response.choices[0].message.content
            
            return {
                'filename': image_info['filename'],
                'image_info': image_info,
                'description': description,
                'model_used': self.model,
                'tokens_used': response.usage.total_tokens if response.usage else None,
                'status': 'success'
            }
            
        except Exception as e:
            return {
                'filename': os.path.basename(image_path),
                'error': str(e),
                'status': 'error'
            }
    
    def process_bulk_images(self, 
                          input_dir: str = None, 
                          output_file: str = None,
                          custom_prompt: Optional[str] = None) -> List[Dict]:
        """
        Process multiple images in bulk and generate descriptions.
        
        Args:
            input_dir: Directory containing images (defaults to assets directory)
            output_file: Output file path for saving results
            custom_prompt: Optional custom prompt
            
        Returns:
            List of description results
        """
        input_dir = input_dir or Config.ASSETS_DIR
        output_file = output_file or os.path.join(Config.DESCRIPTIONS_DIR, 'bulk_descriptions.json')
        
        # Get all image files
        image_files = []
        for ext in Config.SUPPORTED_FORMATS:
            image_files.extend(Path(input_dir).glob(f"*{ext}"))
            image_files.extend(Path(input_dir).glob(f"*{ext.upper()}"))
        
        if not image_files:
            print(f"No supported image files found in {input_dir}")
            return []
        
        print(f"Found {len(image_files)} images to process")
        
        # Process images with progress bar
        results = []
        for image_path in tqdm(image_files, desc="Generating descriptions"):
            result = self.generate_description(str(image_path), custom_prompt)
            results.append(result)
            
            # Save individual result
            individual_output = os.path.join(
                Config.DESCRIPTIONS_DIR, 
                f"{Path(image_path).stem}_description.json"
            )
            with open(individual_output, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
        
        # Save bulk results
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Generate summary
        self._generate_summary(results, output_file)
        
        print(f"Processing complete! Results saved to {output_file}")
        return results
    
    def _generate_summary(self, results: List[Dict], output_file: str):
        """Generate a summary of the bulk processing results."""
        successful = [r for r in results if r.get('status') == 'success']
        failed = [r for r in results if r.get('status') == 'error']
        
        summary = {
            'total_images': len(results),
            'successful': len(successful),
            'failed': len(failed),
            'success_rate': f"{(len(successful) / len(results) * 100):.1f}%" if results else "0%",
            'failed_files': [r['filename'] for r in failed] if failed else []
        }
        
        # Save summary
        summary_file = output_file.replace('.json', '_summary.json')
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        print(f"Summary: {summary['successful']}/{summary['total_images']} images processed successfully")
        if failed:
            print(f"Failed files: {', '.join(summary['failed_files'])}")
    
    def export_to_csv(self, results: List[Dict], output_file: str = None):
        """Export results to CSV format for easy analysis."""
        output_file = output_file or os.path.join(Config.DESCRIPTIONS_DIR, 'descriptions.csv')
        
        # Prepare data for CSV
        csv_data = []
        for result in results:
            if result.get('status') == 'success':
                csv_data.append({
                    'filename': result['filename'],
                    'description': result['description'],
                    'model_used': result.get('model_used', ''),
                    'tokens_used': result.get('tokens_used', ''),
                    'image_format': result.get('image_info', {}).get('format', ''),
                    'image_size': str(result.get('image_info', {}).get('size', ''))
                })
        
        if csv_data:
            df = pd.DataFrame(csv_data)
            df.to_csv(output_file, index=False, encoding='utf-8')
            print(f"CSV export saved to {output_file}")
        else:
            print("No successful results to export to CSV")
    
    def generate_description_with_examples(self, image_path: str, example_images: List[str] = None, example_descriptions: List[str] = None, custom_prompt: Optional[str] = None) -> Dict:
        """
        Generate a visual description using example image-description pairs for better guidance.
        
        Args:
            image_path: Path to the image file to describe
            example_images: List of paths to example images for reference
            example_descriptions: List of corresponding descriptions for the example images
            custom_prompt: Optional custom prompt to override the default
            
        Returns:
            Dictionary containing the description and metadata
        """
        try:
            # Validate image file
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image file not found: {image_path}")
            
            # Validate example inputs
            if example_images and example_descriptions:
                if len(example_images) != len(example_descriptions):
                    raise ValueError("Number of example images must match number of example descriptions")
                
                for example_img in example_images:
                    if not os.path.exists(example_img):
                        raise FileNotFoundError(f"Example image not found: {example_img}")
            
            # Get image info
            image_info = self.get_image_info(image_path)
            
            # Encode target image
            base64_image = self.encode_image(image_path)
            
            # Build messages with examples
            messages = []
            
            # Add system message with examples if provided
            if example_images and example_descriptions:
                system_content = "You are an expert visual describer. Here are examples of the type of description I want:\n\n"
                
                for i, (example_img, example_desc) in enumerate(zip(example_images, example_descriptions)):
                    example_base64 = self.encode_image(example_img)
                    system_content += f"EXAMPLE {i+1}:\n"
                    system_content += f"Image: {os.path.basename(example_img)}\n"
                    system_content += f"Description: {example_desc}\n\n"
                
                messages.append({
                    "role": "system",
                    "content": system_content
                })
            
            # Use custom prompt or default
            prompt = custom_prompt if custom_prompt else Config.ACCESSIBILITY_PROMPT
            
            # Add user message with target image
            user_content = [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
            
            # If we have examples, add them to the user message as well
            if example_images and example_descriptions:
                for example_img in example_images:
                    example_base64 = self.encode_image(example_img)
                    user_content.append({
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{example_base64}"
                        }
                    })
            
            messages.append({
                "role": "user",
                "content": user_content
            })
            
            # Make API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=1000,
                temperature=0.7
            )
            
            description = response.choices[0].message.content
            
            return {
                'filename': image_info['filename'],
                'image_info': image_info,
                'description': description,
                'model_used': self.model,
                'tokens_used': response.usage.total_tokens if response.usage else None,
                'status': 'success',
                'examples_used': len(example_images) if example_images else 0
            }
            
        except Exception as e:
            return {
                'filename': os.path.basename(image_path),
                'error': str(e),
                'status': 'error'
            }

    def process_bulk_images_with_examples(self, 
                                        input_dir: str = None, 
                                        output_file: str = None,
                                        example_images: List[str] = None,
                                        example_descriptions: List[str] = None,
                                        custom_prompt: Optional[str] = None) -> List[Dict]:
        """
        Process multiple images in bulk using example image-description pairs for guidance.
        
        Args:
            input_dir: Directory containing images (defaults to assets directory)
            output_file: Output file path for saving results
            example_images: List of paths to example images for reference
            example_descriptions: List of corresponding descriptions for the example images
            custom_prompt: Optional custom prompt
            
        Returns:
            List of description results
        """
        input_dir = input_dir or Config.ASSETS_DIR
        output_file = output_file or os.path.join(Config.DESCRIPTIONS_DIR, 'bulk_descriptions_with_examples.json')
        
        # Get all image files
        image_files = []
        for ext in Config.SUPPORTED_FORMATS:
            image_files.extend(Path(input_dir).glob(f"*{ext}"))
            image_files.extend(Path(input_dir).glob(f"*{ext.upper()}"))
        
        if not image_files:
            print(f"No supported image files found in {input_dir}")
            return []
        
        print(f"Found {len(image_files)} images to process")
        if example_images:
            print(f"Using {len(example_images)} example images for guidance")
        
        # Process images with progress bar
        results = []
        for image_path in tqdm(image_files, desc="Generating descriptions with examples"):
            result = self.generate_description_with_examples(
                str(image_path), 
                example_images, 
                example_descriptions, 
                custom_prompt
            )
            results.append(result)
            
            # Save individual result
            individual_output = os.path.join(
                Config.DESCRIPTIONS_DIR, 
                f"{Path(image_path).stem}_description_with_examples.json"
            )
            with open(individual_output, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
        
        # Save bulk results
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        # Generate summary
        self._generate_summary(results, output_file)
        
        print(f"Processing complete! Results saved to {output_file}")
        return results 