#!/usr/bin/env python3
"""
Test script for using example images and descriptions with the Art Descriptor.
"""

import sys
import os
from pathlib import Path

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.art_descriptor import ArtDescriptor

def test_with_examples():
    """Test the new generate_description_with_examples function."""
    
    # Initialize art descriptor
    descriptor = ArtDescriptor()
    
    # Example images and descriptions (you can modify these)
    example_images = [
        "examples/example1.jpg",
        "examples/example2.jpg",
        "examples/example3.jpg"
        "examples/example5.jpg"


    ]
    
    example_descriptions = [
        "This vertical print shows the silhouette of a person standing in a doorway, gazing out of a window. The man appears to be dressed in formal attire from a historical period, with a coat and what looks like a high collar or cravat. He wears a white wig. He stands with his hands behind his back in a contemplative pose. The room contains elegant details, including parts of a decorative frame and a small linen-covered table on the left, and a curtain pulled to one side of the window on the right. Through the lower window panes, there appears to be tree foliage visible. The image has a sepia-toned, vintage appearance. Under the image line, on both sides is a small text identifying the artist on the left, and the publisher on the right. At the center of the bottom margin is the title of the work in capital letters “FELIX GRUNDY”. Other smaller text appears beneath it. ",
        "This vertical print is a head and shoulders portrait of a middle-aged woman against a black background. Her head is tilted slightly downward, her long hair combed back from her forehead. She wears a dark dress and a dark blue shawl over her shoulders. Dramatic shadows across the woman’s face, downcast eyes, and prominent cheekbones suggest the person’s physical suffering.",
        "This vertical painting depicts a young woman in a white, draped dress seated by a terrace wall with a view of the green outdoors. The woman wears her hair in an upswept style, her white dress falls in soft, loose folds around her body. She sits on a dark, curved chair, barefoot, with one leg slightly drawn. She holds a ball of blue yarn in her left hand. A winged child-like naked figure stands on the low terrace wall, leans behind the woman, and anoints her ear. She looks up sideways as if towards where she feels the touch, her eyes wide open and lips formed in a soft smile, showing her white teeth. There is a conical woven basket beside her on a tiled floor with several balls of blue yarn, and diagonally across stands a wooden loom with the same color yarn woven through it. A white column rises in the background along the right margin of the picture.",
        "This vertical print depicts an elderly Black woman in a bright home setting. She wears a polka-dotted dress with red, mint green, and brown circles. The woman sits next to a small table against a vivid red wall or background, her feet in simple, brown, laced shoes touching a light green floor. Her face looks tired, with a tightly closed mouth and multiple wrinkles that seem accentuated in black on her resting arms as well. On the three-legged table sits a mint green pot containing a flowering plant painted with black stems and small white blooms. The foreground is divided into a mint green floor and a narrower purple-gray baseboard, creating a striking contrast with the red wall. There is an artist’s signature and date in the upper right corner."

    ]
    
    # Test with a single image
    target_image = "assets/example1.jpg"  # Replace with your target image
    
    print("Testing generate_description_with_examples...")
    result = descriptor.generate_description_with_examples(
        target_image,
        example_images,
        example_descriptions
    )
    
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
    else:
        print(f"Error: {result.get('error', 'Unknown error')}")

def test_bulk_with_examples():
    """Test bulk processing with examples."""
    
    # Initialize art descriptor
    descriptor = ArtDescriptor()
    
    # Example images and descriptions
    example_images = [
        "assets/example1.jpg",
    ]
    
    example_descriptions = [
        "This vertical print shows the silhouette of a person standing in a doorway, gazing out of a window. The man appears to be dressed in formal attire from a historical period, with a coat and what looks like a high collar or cravat. He wears a white wig. He stands with his hands behind his back in a contemplative pose. The room contains elegant details, including parts of a decorative frame and a small linen-covered table on the left, and a curtain pulled to one side of the window on the right. Through the lower window panes, there appears to be tree foliage visible. The image has a sepia-toned, vintage appearance. Under the image line, on both sides is a small text identifying the artist on the left, and the publisher on the right. At the center of the bottom margin is the title of the work in capital letters 'FELIX GRUNDY'. Other smaller text appears beneath it."
    ]
    
    print("\nTesting bulk processing with examples...")
    results = descriptor.process_bulk_images_with_examples(
        example_images=example_images,
        example_descriptions=example_descriptions
    )
    
    print(f"Processed {len(results)} images with examples")

if __name__ == "__main__":
    print("Art Descriptions AI - Example Testing")
    print("=" * 40)
    
    # Test single image with examples
    test_with_examples()
    
    # Test bulk processing with examples
    test_bulk_with_examples() 