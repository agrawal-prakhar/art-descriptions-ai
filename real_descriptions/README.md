# Real Descriptions

This folder contains human-written reference descriptions for artwork images. These serve as ground truth for evaluating AI-generated descriptions.

## Files

- `human_edited.json` - Human-written descriptions for human_edited dataset
- `human_written.json` - Human-written descriptions for human_written dataset
- `README.md` - This file

## Format

Each file contains an array of objects with the following structure:

```json
[
  {
    "filename": "example1.jpg",
    "description": "Detailed human-written description of the artwork..."
  },
  {
    "filename": "example2.jpg",
    "description": "Another detailed description..."
  }
]
```

## Datasets

### human_edited.json
Contains 9 human-written descriptions for images example1.jpg through example9.jpg. These descriptions follow accessibility guidelines and provide comprehensive visual descriptions.

### human_written.json
Contains 10 human-written descriptions for images example1.jpg through example10.jpg. These are original human descriptions used as reference for evaluation.

## Usage

These files are used by the evaluation tools to compare against AI-generated descriptions:

1. **For evaluation**: The `evaluate_cosine_similarity.py` script reads these files
2. **For training**: Can be used as examples for AI model training
3. **For benchmarking**: Serve as ground truth for measuring AI performance

## Guidelines for Human Descriptions

The descriptions in this folder follow accessibility best practices:

- **Comprehensive coverage** of visual elements
- **Logical organization** from general to specific details
- **Clear, descriptive language** that creates mental images
- **Cultural sensitivity** and appropriate terminology
- **Factual accuracy** without interpretation or speculation

## Adding New Datasets

To add a new dataset:

1. **Create a new JSON file** with the same structure
2. **Include all descriptions** for the images in your dataset
3. **Use consistent naming** (e.g., `your_dataset.json`)
4. **Update evaluation scripts** to reference the new file

## Best Practices

1. **Maintain consistency** in description style and length
2. **Use descriptive filenames** that match the image files
3. **Follow accessibility guidelines** for inclusive descriptions
4. **Review and validate** descriptions for accuracy
5. **Document any special considerations** or context

## File Naming Convention

- `{dataset_name}.json` - Human descriptions for a specific dataset
- Match the naming pattern used in `ai_descriptions/` folder
- Use descriptive names that indicate the dataset content 