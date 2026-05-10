import pandas as pd
from datasets import load_dataset

def explore_gutenberg():
    print("Loading Gutenberg Time metadata...")
    # Load only metadata if possible, or just the first few rows
    dataset = load_dataset("community-datasets/gutenberg_time", split="train")
    
    # Gutenberg Time has 'text' and 'year' (or 'guten_id' and we need to map it?)
    # Let's check the columns
    print(f"Columns: {dataset.column_names}")
    
    df = dataset.select(range(1000)).to_pandas()
    print("Sample years:")
    print(df['year'].value_counts().sort_index())
    
    print(f"Total rows: {len(dataset)}")
    
    # Check for sparsity in recent decades (should be 0 for post-1930 if it's really 1930 cutoff)
    # Wait, the dataset might contain modern books too, but Talkie was trained on a filtered version.
    # The literature says Talkie was trained on pre-1931 text.
    
if __name__ == "__main__":
    explore_gutenberg()
