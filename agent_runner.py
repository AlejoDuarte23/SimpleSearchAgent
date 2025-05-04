import asyncio
import pathlib
from agents import Agent, Runner
from agents.mcp import MCPServerStdio
import dotenv
dotenv.load_dotenv()

ROOT = pathlib.Path(__file__).parent
server = MCPServerStdio(params={"command": "python",
                                "args": [str(ROOT / "server.py")]},
                        cache_tools_list=True)

async def main(prompt: str):
    async with server:
        agent = Agent(
            name="Assistant",
            instructions="Use the tool to answer the user.",
            mcp_servers=[server],
        )
        result = await Runner.run(starting_agent=agent, input=prompt)
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main("How to design concrete filled HSS columns? List relevant standards"))
