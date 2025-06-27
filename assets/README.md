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

1. **Add your artwork images** to this folder
2. **Run the processing script**:
   ```bash
   python main.py --bulk
   ```
3. **Check the descriptions folder** for generated outputs

## Tips for Best Results

- Use **high-quality images** for better descriptions
- Ensure images are **well-lit** and **clearly show the artwork**
- **Avoid heavily compressed** or low-resolution images
- For **complex artworks**, consider using **multiple angles** if needed

## Example Structure

```
assets/
├── mona_lisa.jpg
├── starry_night.png
├── the_scream.tiff
└── guernica.webp
```

## Processing

Images in this folder will be automatically detected and processed when you run:
- `python main.py --bulk` (process all images)
- `python main.py --image assets/specific_image.jpg` (process single image)

Generated descriptions will be saved in the `descriptions/` folder. 