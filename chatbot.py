import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "your_api_key_here"
client = OpenAI()

def chatbot():
    print("🤖 Chatbot Agent (type 'exit' to quit)\n")
    history = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        history.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=history
        )
        
        reply = response.choices[0].message.content
        print(f"Bot: {reply}\n")
        
        history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chatbot()
