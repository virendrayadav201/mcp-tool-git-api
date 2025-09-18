from fastmcp import FastMCP
import requests

mcp = FastMCP(name="GitHub MCP")


@mcp.tool(name="get_repo_info", description="Get repository details from GitHub.")
def get_repo_info(owner: str, repo: str, token: str) -> dict:
    """Get repository details from GitHub."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers)
    return resp.json()

@mcp.tool(name="get_repo_commits", description="Get commit details from a GitHub repository.")
def get_repo_commits(owner: str, repo: str, token: str) -> list:
    """Get commit details from a repo."""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {token}"}
    resp = requests.get(url, headers=headers)
    return resp.json()

if __name__ == "__main__":
    mcp.run()