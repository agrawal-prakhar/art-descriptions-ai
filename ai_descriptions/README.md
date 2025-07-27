# Descriptions Folder

This folder contains the generated accessibility descriptions for your artwork images.

## Output Files

When you process images, the following files will be generated:

### Individual Descriptions
- `{filename}_description.json` - Individual description for each image
- Contains detailed metadata and the generated description

### Bulk Processing Results
- `bulk_descriptions.json` - All descriptions in a single file
- `bulk_descriptions_summary.json` - Summary of processing results
- `descriptions.csv` - CSV export (if requested)

## File Structure

```
descriptions/
├── mona_lisa_description.json
├── starry_night_description.json
├── bulk_descriptions.json
├── bulk_descriptions_summary.json
└── descriptions.csv
```

## JSON Output Format

Each description file contains:

```json
{
  "filename": "artwork.jpg",
  "image_info": {
    "format": "JPEG",
    "size": [1920, 1080],
    "mode": "RGB"
  },
  "description": "Detailed accessibility description...",
  "model_used": "gpt-4-vision-preview",
  "tokens_used": 450,
  "status": "success"
}
```

## Summary File

The summary file contains processing statistics:

```json
{
  "total_images": 10,
  "successful": 9,
  "failed": 1,
  "success_rate": "90.0%",
  "failed_files": ["problematic_image.jpg"]
}
```

## Usage

- **JSON files**: Use for programmatic access or detailed analysis
- **CSV file**: Use for spreadsheet analysis or database import
- **Summary**: Quick overview of processing results

## Integration

These descriptions can be integrated into:
- Museum websites
- Audio guides
- Accessibility tools
- Educational materials
- Mobile applications

## Backup

It's recommended to backup these files regularly, especially for large collections. 