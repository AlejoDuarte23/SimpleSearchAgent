# Duck Agent: OpenAI + DuckDuckGo Search with MCP Server

This project demonstrates how to build an OpenAI-powered agent that uses a DuckDuckGo search tool via an MCP server.

## Setup

1. **Clone this repository** (if you haven't already):
   ```sh
   git clone <your-repo-url>
   cd <project-folder>
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key**:
   - Edit the `.env` file and add your OpenAI API key:
     ```env
     OPENAI_API_KEY="sk-..."
     ```

## Running the MCP Server

Start the server (it will listen for tool calls):
```sh
python server.py
```

## Running the Agent

To launch the agent and send a prompt:
```sh
python agent_runner.py
```

The agent will use the DuckDuckGo search tool to answer the prompt and print the result.

---

**Requirements:**
- Python 3.8+
- OpenAI API key

**Main files:**
- `server.py`: Runs the MCP server and exposes the DuckDuckGo search tool.
- `agent_runner.py`: Launches the agent and connects to the server.
