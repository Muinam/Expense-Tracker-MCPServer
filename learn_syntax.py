import random
from fastmcp import FastMCP

# Create the FastMCP server instance
mcp = FastMCP(name='Demo Server')

@mcp.tool
def roll_dice(n_dice: int=1) -> list[int]:
    return [random.randint(1,6) for i in range(n_dice)]


@mcp.tool
def add_number(a : float, b: float) -> float:
    return a + b

if __name__ == "__main__":
    mcp.run()