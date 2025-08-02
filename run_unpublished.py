#!/usr/bin/env python3
"""
Simple script to run process_bulk_images_with_examples with examples from human_written.json
"""

import json
import os
from src.art_descriptor import ArtDescriptor

# Load examples from human_written.json
with open('real_descriptions/human_written.json', 'r') as f:
    examples_data = json.load(f)

# Prepare example images and descriptions
example_images = []
example_descriptions = []

for item in examples_data:
    image_path = os.path.join('assets/human_written', item['filename'])
    example_images.append(image_path)
    example_descriptions.append(item['description'])

print(f"Loaded {len(example_images)} examples from human_written.json")

# Initialize ArtDescriptor and run the function
descriptor = ArtDescriptor()

results = descriptor.process_bulk_images_with_examples(
    input_dir='assets/unpublished',
    output_file='ai_descriptions/unpublished_with_human_examples.json',
    example_images=example_images,
    example_descriptions=example_descriptions
)

print(f"Processing complete! Generated descriptions for {len(results)} images.") 