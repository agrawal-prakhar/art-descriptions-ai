# Evaluation Tools

This folder contains tools for evaluating the quality of AI-generated descriptions by comparing them with human-written reference descriptions.

## Files

- `evaluate_cosine_similarity.py` - Main evaluation script
- `requirements.txt` - Dependencies for evaluation
- `README.md` - This file

## Cosine Similarity Evaluation

The evaluation script compares AI-generated descriptions with human-written reference descriptions using semantic similarity.

### Setup

1. **Install dependencies**:
   ```bash
   pip install -r evaluation/requirements.txt
   ```

2. **Prepare your data**:
   - Real descriptions: `real_descriptions/human_written.json`
   - AI descriptions: `ai_descriptions/human_written.json`

### Usage

Run the evaluation script:
```bash
cd evaluation
python evaluate_cosine_similarity.py
```

### Output

The script generates `similarity_result_human_written.json` with cosine similarity scores:

```json
[
  {
    "filename": "example1.jpg",
    "cosine_similarity": 0.85
  },
  {
    "filename": "example2.jpg",
    "cosine_similarity": 0.72
  }
]
```

### Model Used

The evaluation uses the `all-MiniLM-L6-v2` sentence transformer model:
- **Type**: Sentence embedding model
- **Architecture**: Based on MiniLM (distilled BERT)
- **Size**: ~80MB
- **Dimensions**: 384-dimensional embeddings
- **Performance**: Fast and efficient for semantic similarity

### Interpreting Results

- **Higher scores (0.8-1.0)**: High semantic similarity
- **Medium scores (0.6-0.8)**: Moderate similarity
- **Lower scores (0.0-0.6)**: Low similarity

### Customization

To evaluate different datasets, modify the file paths in `evaluate_cosine_similarity.py`:

```python
REAL_DESCRIPTIONS_PATH = '../real_descriptions/your_dataset.json'
AI_DESCRIPTIONS_PATH = '../ai_descriptions/your_dataset.json'
OUTPUT_PATH = 'similarity_result_your_dataset.json'
```

## Best Practices

1. **Use consistent naming** between real and AI description files
2. **Ensure descriptions match** the same images in both files
3. **Review low similarity scores** to identify potential issues
4. **Use multiple evaluation metrics** for comprehensive assessment

## Troubleshooting

**"No AI description found for {filename}"**
- Check that the AI descriptions file contains the same filenames
- Verify the file paths are correct

**Import errors**
- Make sure you've installed the evaluation requirements
- Check that sentence-transformers is properly installed 