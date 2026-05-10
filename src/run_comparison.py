import os
import json
from talkie import Talkie, Message

def run_humaneval_on_model(model_name, is_it=True):
    print(f"Loading {model_name}...")
    model = Talkie(model_name)
    
    tasks = [
        {
            "id": "add",
            "prompt": "def add(a, b):\n    \"\"\"Return the sum of a and b\"\"\"\n",
        },
        {
            "id": "reverse",
            "prompt": "def reverse_string(s):\n    \"\"\"Return the reverse of string s\"\"\"\n",
        }
    ]
    
    results = []
    
    # 0-shot
    print(f"Running {model_name} 0-shot...")
    for task in tasks:
        if is_it:
            messages = [Message(role="user", content=f"Complete the following Python function:\n\n{task['prompt']}")]
            response = model.chat(messages, max_tokens=50, temperature=0.1)
            results.append({"task": task['id'], "shots": 0, "code": response.text})
        else:
            # Base model completion
            prompt = f"Complete the following Python function:\n\n{task['prompt']}"
            response = model.generate(prompt, max_tokens=50, temperature=0.1)
            results.append({"task": task['id'], "shots": 0, "code": response.text})
            
    # 3-shot
    print(f"Running {model_name} 3-shot...")
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
        prompt = few_shot_context + task['prompt']
        if is_it:
            messages = [Message(role="user", content=prompt)]
            response = model.chat(messages, max_tokens=50, temperature=0.1)
        else:
            response = model.generate(prompt, max_tokens=50, temperature=0.1)
        results.append({"task": task['id'], "shots": 3, "code": response.text})
        
    return results

def main():
    # Run on Talkie-1930 (Vintage)
    vintage_results = run_humaneval_on_model("talkie-1930-13b-it", is_it=True)
    
    # Run on Talkie-Web (Modern)
    modern_results = run_humaneval_on_model("talkie-web-13b-base", is_it=False)
    
    os.makedirs("results", exist_ok=True)
    with open("results/comparison_humaneval.json", "w") as f:
        json.dump({
            "vintage": vintage_results,
            "modern": modern_results
        }, f, indent=2)
    print("Comparison complete.")

if __name__ == "__main__":
    main()
