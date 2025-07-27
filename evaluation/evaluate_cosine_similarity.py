import json
import os
from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Paths
REAL_DESCRIPTIONS_PATH = os.path.join(os.path.dirname(__file__), 'real_descriptions.json')
AI_DESCRIPTIONS_PATH = os.path.join(os.path.dirname(__file__), '../descriptions/bulk_descriptions.json')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'cosine_similarity_report.csv')

# Load real/ideal descriptions
def load_real_descriptions(path):
    with open(path, 'r', encoding='utf-8') as f:
        return {item['filename']: item['description'] for item in json.load(f)}

# Load AI-generated descriptions
def load_ai_descriptions(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return {item['filename']: item['description'] for item in data}

def main():
    # Load data
    real_desc = load_real_descriptions(REAL_DESCRIPTIONS_PATH)
    ai_desc = load_ai_descriptions(AI_DESCRIPTIONS_PATH)

    # Initialize model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    results = []
    # Only process example1.jpg
    filename = "example1.jpg"
    real_text = real_desc.get(filename)
    ai_text = ai_desc.get(filename)
    
    if not real_text:
        print(f"No real description found for {filename}")
        return
    
    if not ai_text:
        print(f"No AI description found for {filename}")
        return
    
    # Compute embeddings
    emb_real = model.encode(real_text, convert_to_tensor=True)
    emb_ai = model.encode(ai_text, convert_to_tensor=True)
    # Cosine similarity
    similarity = util.pytorch_cos_sim(emb_real, emb_ai).item()
    results.append({
        'filename': filename,
        'cosine_similarity': similarity
    })

    # Save results
    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Cosine similarity report saved to {OUTPUT_PATH}")

if __name__ == '__main__':
    main() 