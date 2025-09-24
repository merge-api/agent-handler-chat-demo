from merge_mcp import AgentHandler, MCPServer
from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "your_api_key_here"
client = OpenAI()

class ChatbotHandler(AgentHandler):
    async def handle(self, request):
        user_input = request["input"]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        return {"output": response.choices[0].message.content}

if __name__ == "__main__":
    server = MCPServer(agent_handler=ChatbotHandler())
    server.run()
