# AI Descriptions

This folder contains AI-generated descriptions for artwork images. These are created by the Art Descriptions AI system using OpenAI's GPT-4 Vision API.

## Files

- `human_edited.json` - AI descriptions for human_edited dataset
- `human_written.json` - AI descriptions for human_written dataset
- `README.md` - This file

## Format

Each file contains an array of objects with the following structure:

```json
[
  {
    "filename": "example1.jpg",
    "description": "AI-generated description of the artwork..."
  },
  {
    "filename": "example2.jpg",
    "description": "Another AI-generated description..."
  }
]
```

## Generation

These files are automatically generated when you run:

```bash
# Generate descriptions for a specific dataset
python main.py --bulk --input-dir assets/human_edited

# Generate descriptions with examples
python main.py --bulk --input-dir assets/human_edited --with-examples
```

## Auto-naming Convention

The output files are automatically named based on the input directory:

- `assets/human_edited/` → `ai_descriptions/human_edited.json`
- `assets/human_written/` → `ai_descriptions/human_written.json`
- `assets/your_dataset/` → `ai_descriptions/your_dataset.json`

## Evaluation

These AI descriptions are used for evaluation against human-written reference descriptions:

1. **Cosine similarity evaluation**: Compare semantic similarity with human descriptions
2. **Quality assessment**: Measure AI performance and accuracy
3. **Iterative improvement**: Use results to refine prompts and models

## Features

- **Simplified output**: Only filename and description (no metadata)
- **Accessibility-focused**: Generated using specialized accessibility prompts
- **Consistent format**: Standardized JSON structure for easy processing
- **Auto-generated**: Files are created automatically during processing

## Best Practices

1. **Review generated descriptions** for accuracy and appropriateness
2. **Compare with human descriptions** using evaluation tools
3. **Iterate on prompts** based on evaluation results
4. **Backup important results** before regenerating
5. **Use consistent naming** for easy organization

## File Management

- **Keep organized**: Use descriptive dataset names
- **Version control**: Track changes to generated descriptions
- **Backup regularly**: Save important results
- **Document context**: Note any special processing or prompts used

## Troubleshooting

**Missing files**: Ensure the input directory exists and contains images
**Empty descriptions**: Check API key and model configuration
**Inconsistent naming**: Verify input directory names match expected patterns 