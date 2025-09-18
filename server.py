import os
from dotenv import load_dotenv
from fastmcp import FastMCP
from github import Github, Auth

# Read GitHub token from env
load_dotenv()
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise RuntimeError("Please set environment variable GITHUB_TOKEN")

gh = Github(auth=Auth.Token(GITHUB_TOKEN))

mcp = FastMCP("GitHubRepoServer")

@mcp.tool
def list_files(repo_name: str, path: str = "") -> list[str]:
    """
    List files in a GitHub repository under a given path.
    repo_name: like "username/repo"
    path: directory path inside the repo ("" for root)
    """
    repo = gh.get_repo(repo_name)
    contents = repo.get_contents(path)
    return [content.path for content in contents]

@mcp.tool
def get_file(repo_name: str, file_path: str) -> str:
    """
    Get the content of a file in a GitHub repo.
    repo_name: "username/repo"
    file_path: path to file in the repo, e.g. "src/myfile.py"
    """
    repo = gh.get_repo(repo_name)
    content_file = repo.get_contents(file_path)
    return content_file.decoded_content.decode("utf-8")


@mcp.tool
def clone_repo(repo_name: str, local_dir: str) -> str:
    """
    Clones the repo locally via Git, into local_dir.
    Returns a message showing success or error.
    """
    import subprocess
    try:
        subprocess.run(
            ["git", "clone", f"https://github.com/{repo_name}.git", local_dir],
            check=True,
        )
        return f"Cloned {repo_name} into {local_dir}"
    except subprocess.CalledProcessError as e:
        return f"Error cloning: {e}"

if __name__ == "__main__":
    mcp.run()
