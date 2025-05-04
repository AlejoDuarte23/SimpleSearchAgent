from fastmcp import FastMCP
from duckduckgo_search import DDGS

mcp = FastMCP("DuckSearch")

@mcp.tool()
def duck_search(query: str, n_results: int = 5):
    with DDGS() as d:
        return [{"title": r["title"], "url": r["href"], "snippet": r["body"]}
                for r in d.text(query, max_results=n_results)]

if __name__ == "__main__":
    mcp.run()
