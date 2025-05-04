# Duck Agent: Simple Tutorial

This project shows how to make a smart agent that can search the web using DuckDuckGo and answer your questions. It uses OpenAI and the FastMCP server.

---

## What you need
- Python 3.8 or newer
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

---

## 1. Install the tools
Open your terminal. Go to this folder. Run:
```sh
pip install -r requirements.txt
```
This command installs all the Python packages you need. If you see errors, make sure you have Python 3.8 or newer.

---

## 2. Add your OpenAI key
Open the `.env` file in this folder. You will see a line like this:
```
OPENAI_API_KEY=sk-xxxxxx
```
Replace `sk-xxxxxx` with your real OpenAI API key. This key lets the agent use OpenAI to answer questions.

---

## 3. Start the search server
The server lets the agent search the web for you. It uses DuckDuckGo to find answers.
Run this command:
```sh
python server.py
```
You should see the server start. Leave this terminal open. The server waits for the agent to ask for web searches.

---

## 4. Run the agent
Open a new terminal window or tab. In the same folder, run:
```sh
python agent_runner.py
```
The agent will connect to the server, ask a question, and print the answer. You can change the question in `agent_runner.py` if you want.

---

## What do these files do?
- `requirements.txt`: Lists all the Python packages you need.
- `.env`: Stores your OpenAI API key. Keep this file secret!
- `server.py`: Runs the FastMCP server and lets the agent search the web.
- `agent_runner.py`: Starts the agent, connects to the server, and asks a question.

---

## Learn more
- [FastMCP docs](https://github.com/jlowin/fastmcp) – How the server works
- [OpenAI Agents guide](https://platform.openai.com/docs/guides/agents) – How agents work
- [OpenAI Agents Python docs](https://openai.github.io/openai-agents-python/) – Python library for agents
- [OpenAI Agents MCP docs](https://openai.github.io/openai-agents-python/mcp/) – Using MCP with agents

---

**Tip:**
If you see errors about missing packages, run the install command again. If you see errors about your API key, check your `.env` file.

**You did it!** Now you have a smart agent that can search the web for you. Try changing the question in `agent_runner.py` and see what happens!
