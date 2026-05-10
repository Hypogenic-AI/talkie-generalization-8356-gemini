import os
from datasets import load_dataset
from talkie import download_model

def setup():
    # Create datasets directory if it doesn't exist
    os.makedirs("datasets", exist_ok=True)
    
    print("Downloading Gutenberg Time...")
    try:
        dataset = load_dataset("community-datasets/gutenberg_time", trust_remote_code=True)
        # Note: gutenberg_time is very large (~50k books). 
        # For this research, we might only need a sample or just metadata.
        # But let's try to load it first.
        print("Gutenberg Time loaded.")
    except Exception as e:
        print(f"Error loading Gutenberg Time: {e}")

    print("Downloading HumanEval...")
    try:
        dataset = load_dataset("openai/humaneval", trust_remote_code=True)
        dataset.save_to_disk("datasets/humaneval")
        print("HumanEval saved.")
    except Exception as e:
        print(f"Error loading HumanEval: {e}")

    print("Downloading MMLU...")
    try:
        # Load a subset of MMLU to save time/space
        # Or load 'all' if we need broad coverage
        dataset = load_dataset("cais/mmlu", "all", trust_remote_code=True)
        dataset.save_to_disk("datasets/mmlu")
        print("MMLU saved.")
    except Exception as e:
        print(f"Error loading MMLU: {e}")

    print("Downloading Talkie-1930-13b-it model...")
    try:
        download_model("talkie-1930-13b-it")
        print("Model downloaded.")
    except Exception as e:
        print(f"Error downloading model: {e}")

if __name__ == "__main__":
    setup()
