from fastmcp import FastMCP

mcp = FastMCP("addition")

# Pure Python implementation that is safe to call from the CLI or other code
# def add_impl(a: int, b: int) -> int:
#     """This is the tool which performs addition and this should be used whenever addion"""
#     return a + b

# Register a tool that forwards to the pure implementation. The decorator
# may replace the function object with a tool wrapper, so we keep the
# callable implementation in `add_impl` and expose it to local callers via
# the `add` name below.
@mcp.tool(name="jodo", description="This is the tool which performs addition")
def add_tool(a, b):
    """This is the tool which performs addition and this should be used whenever addion"""
    return "dono jodne ke baad"+f"{a}+{b}={a+b}"

if __name__ == "__main__":
    mcp.serve()