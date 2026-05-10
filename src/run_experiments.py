import os
import json
import pandas as pd
from datasets import load_from_disk, load_dataset
from tqdm import tqdm
from talkie import Talkie, Message
import torch

def run_mmlu_eval(model, subjects, num_samples=20):
    results = {}
    
    # Try to load from disk if saved, otherwise load from hub
    try:
        dataset_all = load_from_disk("datasets/mmlu")
    except:
        dataset_all = load_dataset("cais/mmlu", "all", trust_remote_code=True)

    for subject in subjects:
        print(f"Evaluating subject: {subject}")
        # MMLU subjects are usually in the 'subject' column if using 'all'
        # Actually cais/mmlu/all has everything in one.
        # Let's filter by subject if available, or just use the sub-datasets.
        try:
            # Re-loading specific sub-dataset for convenience
            ds = load_dataset("cais/mmlu", subject, split="test", trust_remote_code=True)
        except:
            print(f"Could not load {subject}, skipping.")
            continue
            
        correct = 0
        total = min(num_samples, len(ds))
        
        for i in range(total):
            item = ds[i]
            question = item['question']
            choices = item['choices']
            answer_idx = item['answer']
            answer_label = chr(65 + answer_idx) # 0 -> A, 1 -> B, etc.
            
            prompt = f"The following is a multiple choice question about {subject.replace('_', ' ')}.\n\n"
            prompt += f"Question: {question}\n"
            for j, choice in enumerate(choices):
                prompt += f"{chr(65+j)}. {choice}\n"
            prompt += "\nAnswer with only the letter of the correct option.\nAnswer:"
            
            messages = [Message(role="user", content=prompt)]
            response = model.chat(messages, max_tokens=5, temperature=0.1)
            pred = response.text.strip().upper()
            
            # Simple check: does the response contain the correct letter?
            if answer_label in pred[:5]:
                correct += 1
                
        results[subject] = correct / total
        print(f"Result for {subject}: {results[subject]:.2f}")
        
    return results

def run_humaneval_mini(model):
    # Manually defined subset of HumanEval-like tasks
    # Task 1: Addition (Pre-1930 logic)
    # Task 2: String reversal (Pre-1930 logic)
    # Task 3: List filtering (Modern syntax, basic logic)
    
    tasks = [
        {
            "id": "add",
            "prompt": "def add(a, b):\n    \"\"\"Return the sum of a and b\"\"\"\n",
            "test": "assert add(2, 3) == 5"
        },
        {
            "id": "reverse",
            "prompt": "def reverse_string(s):\n    \"\"\"Return the reverse of string s\"\"\"\n",
            "test": "assert reverse_string('hello') == 'olleh'"
        },
        {
            "id": "filter_even",
            "prompt": "def filter_even(numbers):\n    \"\"\"Return a list containing only the even numbers from the input list\"\"\"\n",
            "test": "assert filter_even([1, 2, 3, 4]) == [2, 4]"
        }
    ]
    
    results = []
    
    # 0-shot
    print("Running HumanEval 0-shot...")
    for task in tasks:
        messages = [Message(role="user", content=f"Complete the following Python function:\n\n{task['prompt']}")]
        response = model.chat(messages, max_tokens=100, temperature=0.1)
        results.append({"task": task['id'], "shots": 0, "code": response.text})
        
    # 3-shot
    print("Running HumanEval 3-shot...")
    few_shot_context = """Complete the following Python functions:

def multiply(a, b):
    \"\"\"Return the product of a and b\"\"\"
    return a * b

def is_positive(n):
    \"\"\"Check if n is positive\"\"\"
    return n > 0

def get_length(s):
    \"\"\"Return the length of string s\"\"\"
    return len(s)

"""
    for task in tasks:
        prompt = few_shot_context + f"def {task['id']}" + task['prompt'].split(f"def {task['id']}")[-1]
        messages = [Message(role="user", content=prompt)]
        response = model.chat(messages, max_tokens=100, temperature=0.1)
        results.append({"task": task['id'], "shots": 3, "code": response.text})
        
    return results

def main():
    print("Initializing model...")
    model = Talkie("talkie-1930-13b-it")
    
    # MMLU Experiment
    pre_1930_subjects = ["ancient_history", "world_religions", "philosophy"]
    post_1930_subjects = ["computer_science", "college_computer_science", "genetics"]
    
    subjects = pre_1930_subjects + post_1930_subjects
    mmlu_results = run_mmlu_eval(model, subjects)
    
    # HumanEval Experiment
    he_results = run_humaneval_mini(model)
    
    # Save results
    os.makedirs("results", exist_ok=True)
    with open("results/mmlu_results.json", "w") as f:
        json.dump(mmlu_results, f, indent=2)
    with open("results/humaneval_results.json", "w") as f:
        json.dump(he_results, f, indent=2)
        
    print("Experiments complete. Results saved to results/")

if __name__ == "__main__":
    main()
