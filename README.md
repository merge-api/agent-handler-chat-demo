# Agent Handler Chat Demo

This repo provides three ready-to-run examples:

1. **chatbot.py** — Minimal OpenAI chatbot loop (paste your API key and run).  
2. **agent_handler.py** — Implements a custom AgentHandler using Merge MCP's Python SDK.  
3. **mcp_client.py** — Async MCP client that connects to an MCP server, lists tools, and can call them.  

## 🚀 Quickstart

```bash
# Clone repo
git clone https://github.com/merge-api/agent-handler-chat-demo.git
cd agent-handler-chat-demo

# Install dependencies
pip install -r requirements.txt

# Run chatbot
python chatbot.py

# Run agent handler (server mode)
python agent_handler.py

# Run MCP client
python mcp_client.py
```

## 🔑 Setup

- Replace `your_api_key_here` with your OpenAI API key in `chatbot.py` and `agent_handler.py`.
- Replace `<auth_token>`, `<tool_pack_id>`, `<registered_user_id>` in `mcp_client.py` with your values.

## 📁 Project Structure

```
agent-handler-chat-demo/
├── README.md
├── requirements.txt
├── chatbot.py
├── agent_handler.py
└── mcp_client.py
```

## 📄 File Descriptions

- **chatbot.py**: Simple interactive chatbot using OpenAI's API
- **agent_handler.py**: MCP-compatible agent handler server
- **mcp_client.py**: Async MCP client for connecting to MCP servers
- **requirements.txt**: Python dependencies
- **README.md**: This file with setup instructions
