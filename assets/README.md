# Assets Folder

This folder is where you should place your artwork images for processing.

## Supported Formats

The system supports the following image formats:
- JPG/JPEG
- PNG
- GIF
- BMP
- TIFF
- WebP

## Usage

### Basic Usage
1. **Add your artwork images** to this folder
2. **Run the processing script**:
   ```bash
   python main.py --bulk
   ```
3. **Check the ai_descriptions folder** for generated outputs

### Organized Usage
1. **Create subdirectories** for different image sets:
   ```
   assets/
   ├── human_edited/     # Images for human_edited dataset
   ├── human_written/    # Images for human_written dataset
   └── your_dataset/     # Your custom dataset
   ```

2. **Process specific directories**:
   ```bash
   python main.py --bulk --input-dir assets/human_edited
   ```

3. **Output files** will be automatically named:
   - `ai_descriptions/human_edited.json`
   - `ai_descriptions/human_written.json`
   - `ai_descriptions/your_dataset.json`

## Tips for Best Results

- Use **high-quality images** for better descriptions
- Ensure images are **well-lit** and **clearly show the artwork**
- **Avoid heavily compressed** or low-resolution images
- For **complex artworks**, consider using **multiple angles** if needed
- **Organize images** in subdirectories for easier management

## Example Structure

```
assets/
├── human_edited/
│   ├── example1.jpg
│   ├── example2.jpg
│   └── example3.jpg
├── human_written/
│   ├── example1.jpg
│   ├── example2.jpg
│   └── example3.jpg
└── custom_dataset/
    ├── artwork1.jpg
    ├── artwork2.png
    └── artwork3.tiff
```

## Processing

Images in this folder will be automatically detected and processed when you run:
- `python main.py --bulk` (process all images in assets/)
- `python main.py --bulk --input-dir assets/human_edited` (process specific subdirectory)
- `python main.py --image assets/specific_image.jpg` (process single image)

Generated descriptions will be saved in the `ai_descriptions/` folder with filenames matching the input directory names. 