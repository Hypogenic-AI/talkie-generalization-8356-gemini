import json
from datasets import load_dataset
from talkie import Talkie, Message

def debug_mmlu():
    model = Talkie("talkie-1930-13b-it")
    subject = "college_computer_science"
    ds = load_dataset("cais/mmlu", subject, split="test", trust_remote_code=True)
    
    for i in range(10):
        item = ds[i]
        question = item['question']
        choices = item['choices']
        answer_idx = item['answer']
        answer_label = chr(65 + answer_idx)
        
        prompt = f"The following is a multiple choice question about {subject.replace('_', ' ')}.\n\n"
        prompt += f"Question: {question}\n"
        for j, choice in enumerate(choices):
            prompt += f"{chr(65+j)}. {choice}\n"
        prompt += "\nAnswer with only the letter of the correct option.\nAnswer:"
        
        messages = [Message(role="user", content=prompt)]
        response = model.chat(messages, max_tokens=5, temperature=0.1)
        pred = response.text.strip().upper()
        
        print(f"Q: {question}")
        print(f"Pred: {pred}, Actual: {answer_label}")
        print("-" * 20)

if __name__ == "__main__":
    debug_mmlu()
