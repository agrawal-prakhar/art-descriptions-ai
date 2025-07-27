# Art Descriptions AI

An AI-powered system for generating accessibility-focused visual descriptions of artwork images using OpenAI's GPT-4 Vision API. This tool is specifically designed to help museums and cultural institutions create detailed, engaging descriptions for visitors with visual impairments.

## Features

- **Accessibility-Focused**: Specialized prompts designed for people with visual impairments
- **Bulk Processing**: Process multiple images efficiently with progress tracking
- **Simplified Output**: Clean JSON format with just filename and description
- **Custom Prompts**: Use your own prompts or the built-in accessibility-focused ones
- **Evaluation Tools**: Built-in cosine similarity evaluation for comparing AI vs human descriptions
- **Error Handling**: Robust error handling with detailed logging

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd art-descriptions-ai

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file in the project root:

```bash
# Copy the example environment file
cp env.example .env

# Edit .env and add your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Add Images

Place your artwork images in the `assets/` folder or create subdirectories like `assets/human_edited/`. Supported formats:
- JPG/JPEG
- PNG
- GIF
- BMP
- TIFF
- WebP

### 4. Generate Descriptions

#### Process all images in a directory:
```bash
python main.py --bulk --input-dir assets/human_edited
```

#### Process a single image:
```bash
python main.py --image assets/your_artwork.jpg
```

#### Use a custom prompt:
```bash
python main.py --bulk --input-dir assets/human_edited --prompt "Describe this artwork focusing on its historical significance"
```

## Usage Examples

### Command Line Interface

```bash
# List all supported images
python main.py --list-images

# Process with custom input directory
python main.py --bulk --input-dir assets/human_edited

# Process single image with custom prompt
python main.py --image artwork.jpg --prompt "Focus on the emotional impact of this piece"
```

### Programmatic Usage

```python
from src.art_descriptor import ArtDescriptor

# Initialize the descriptor
descriptor = ArtDescriptor()

# Process a single image
result = descriptor.generate_description("assets/artwork.jpg")

# Process multiple images
results = descriptor.process_bulk_images(input_dir="assets/human_edited")
```

## Output Structure

### Simplified JSON Output
```json
[
  {
    "filename": "example1.jpg",
    "description": "This magnificent oil painting depicts..."
  },
  {
    "filename": "example2.jpg",
    "description": "This vertical print shows..."
  }
]
```

### Auto-generated Output Files
- `ai_descriptions/{directory_name}.json` - AI-generated descriptions
- `ai_descriptions/{directory_name}_with_examples.json` - Descriptions with examples

## Evaluation

### Cosine Similarity Evaluation

Compare AI-generated descriptions with human-written descriptions:

```bash
# Install evaluation dependencies
pip install -r evaluation/requirements.txt

# Run evaluation
cd evaluation && python evaluate_cosine_similarity.py
```

This will generate `similarity_result_human_written.json` with cosine similarity scores.

## Accessibility Features

The system uses specialized prompts designed for accessibility:

- **Comprehensive Coverage**: Describes composition, subject matter, visual elements, style, emotional impact, and cultural significance
- **Vivid Language**: Uses descriptive language that creates mental images
- **Logical Flow**: Organized from general to specific details
- **Cultural Context**: Includes historical and cultural significance
- **Emotional Engagement**: Captures the mood and atmosphere of artworks

## Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `OPENAI_MODEL` | Model to use for analysis | `gpt-4o` |
| `OUTPUT_FORMAT` | Output format preference | `json` |
| `OUTPUT_DIR` | Output directory | `descriptions` |

### Supported Image Formats

- `.jpg`, `.jpeg`
- `.png`
- `.gif`
- `.bmp`
- `.tiff`
- `.webp`

## Project Structure

```
art-descriptions-ai/
├── assets/                 # Place your artwork images here
│   ├── human_edited/      # Example: human_edited images
│   └── human_written/     # Example: human_written images
├── ai_descriptions/        # AI-generated descriptions
│   ├── human_edited.json  # AI descriptions for human_edited
│   └── human_written.json # AI descriptions for human_written
├── real_descriptions/      # Human-written reference descriptions
│   ├── human_edited.json  # Human descriptions for human_edited
│   └── human_written.json # Human descriptions for human_written
├── evaluation/             # Evaluation tools
│   ├── evaluate_cosine_similarity.py
│   └── requirements.txt
├── similarity_results/     # Evaluation results
├── src/                   # Source code
│   ├── __init__.py
│   ├── config.py          # Configuration and settings
│   └── art_descriptor.py  # Main functionality
├── main.py                # Command-line interface
├── example_usage.py       # Usage examples
├── requirements.txt       # Python dependencies
├── env.example           # Environment variables template
└── README.md             # This file
```

## API Usage and Costs

This system uses OpenAI's GPT-4 Vision API. Costs depend on:
- Number of images processed
- Complexity of descriptions
- Image resolution and detail

**Estimated costs**: ~$0.01-0.03 per image (varies by image complexity)

## Best Practices

1. **Image Quality**: Use high-quality images for better descriptions
2. **Batch Processing**: Process images in batches to manage API costs
3. **Custom Prompts**: Tailor prompts to your specific collection or audience
4. **Review Outputs**: Always review generated descriptions for accuracy
5. **Backup Results**: Keep backups of your generated descriptions
6. **Evaluation**: Use the built-in evaluation tools to assess AI performance

## Troubleshooting

### Common Issues

**"OPENAI_API_KEY is required"**
- Make sure you've created a `.env` file with your API key

**"No supported image files found"**
- Check that your images are in the supported formats
- Verify the images are in the correct directory

**API Rate Limits**
- The system includes built-in error handling for rate limits
- Consider processing smaller batches if you encounter limits

**Memory Issues with Large Images**
- The system automatically handles image encoding
- Very large images may take longer to process

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the example usage
3. Open an issue on GitHub

---

**Note**: This tool is designed to assist in creating accessible content but should be reviewed by human experts, especially for cultural sensitivity and accuracy.