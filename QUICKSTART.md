# Quick Start Guide

Get up and running with Art Descriptions AI in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set Up Your API Key

1. Copy the environment template:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

## Step 3: Add Your Artwork Images

Place your artwork images in the `assets/` folder:

```bash
# Example: Copy your images to the assets folder
cp /path/to/your/artwork/*.jpg assets/
```

**Supported formats**: JPG, PNG, GIF, BMP, TIFF, WebP

## Step 4: Generate Descriptions

### Option A: Process All Images at Once
```bash
python main.py --bulk
```

### Option B: Process a Single Image
```bash
python main.py --image assets/your_artwork.jpg
```

### Option C: Export to CSV for Easy Analysis
```bash
python main.py --bulk --export-csv
```

## Step 5: Check Your Results

Your generated descriptions will be saved in the `descriptions/` folder:

- `bulk_descriptions.json` - All descriptions in one file
- `bulk_descriptions_summary.json` - Processing summary
- `descriptions.csv` - CSV export (if requested)
- Individual files for each image

## Example Workflow

```bash
# 1. Test your setup
python test_setup.py

# 2. List available images
python main.py --list-images

# 3. Process all images with progress tracking
python main.py --bulk

# 4. Export to CSV for spreadsheet analysis
python main.py --bulk --export-csv

# 5. Check the results
ls descriptions/
cat descriptions/bulk_descriptions_summary.json
```

## Customization

### Use a Custom Prompt
```bash
python main.py --bulk --prompt "Focus on the historical significance and cultural context of this artwork"
```

### Process Images from a Different Folder
```bash
python main.py --bulk --input-dir my_artwork_folder
```

### Save Results to a Custom Location
```bash
python main.py --bulk --output-file my_results.json
```

## What You Get

Each generated description includes:

- **Comprehensive visual description** (200-400 words)
- **Accessibility-focused language** for people with visual impairments
- **Artistic analysis** including style, technique, and cultural context
- **Metadata** including image info, tokens used, and processing status

## Troubleshooting

**"OPENAI_API_KEY is required"**
- Make sure you created the `.env` file and added your API key

**"No supported image files found"**
- Check that your images are in the supported formats
- Verify they're in the `assets/` folder

**API Rate Limits**
- The system handles rate limits automatically
- Process smaller batches if needed

## Next Steps

- Review generated descriptions for accuracy
- Customize prompts for your specific collection
- Integrate descriptions into your museum website
- Consider using the programmatic interface for automation

---

**Need help?** Check the main README.md for detailed documentation and examples. 