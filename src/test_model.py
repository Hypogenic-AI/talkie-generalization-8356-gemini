from talkie import Talkie

def test():
    print("Loading Talkie-1930-13b-it...")
    try:
        model = Talkie("talkie-1930-13b-it")
        print("Model loaded.")
        
        prompt = "User: What is the capital of France?\nAssistant:"
        # Talkie IT model might expect a specific format.
        # Checking talkie/chat.py or README for chat format.
        # README says:
        # messages = [Message(role="user", content="...")]
        # result = model.chat(messages)
        
        from talkie import Message
        messages = [Message(role="user", content="What is the capital of France?")]
        result = model.chat(messages, max_tokens=50)
        print(f"Response: {result.text}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test()
