# main.py
import sys
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """一律加 10"""
    return a + b + 10


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Problem 1，python 讀到 3.9.6， MCP 至少要 3.10
#    確認後版本是 3.12
#    如果是 3.10 以上，則可以啟動 MCP server

# Problem 2， 一開始沒有啟動 server
if __name__ == "__main__":
    print("MCP server is starting...", file=sys.stderr)
    mcp.run()



# claude_desktop_config.json
# 最一開始的設定檔，但這樣會讀到 pythin 9.6，啟動不了
# {
#   "mcpServers": {
#     "Demo": {
#       "command": "/opt/homebrew/bin/uv",
#       "args": [
#         "run",
#         "--with",
#         "mcp[cli]",
#         "mcp",
#         "run",
#         "/Users/duncan/code/python/mcp-server-demo/main.py"
#       ]
#     }
#   }
# }

# 後來改這樣
# {
#   "mcpServers": {
#     "Demo": {
#       "command": "/Users/duncan/code/python/mcp-server-demo/.venv/bin/python",
#       "args": [
#         "/Users/duncan/code/python/mcp-server-demo/main.py"
#       ]
#     }
#   }
# }
