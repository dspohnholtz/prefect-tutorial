# This is an example workflow from the Prefect quickstart
# Link: https://docs.prefect.io/v3/get-started/quickstart

import httpx

from prefect import flow, task

@flow(name="first_flow", log_prints=True)
def show_stars(github_repos: list[str]):
    """
    Show the number of stars that GitHub repos have
    """
    for repo in github_repos:
        # Call Task 1
        repo_stats = fetch_stats(repo)
        
        # Call Task 2
        stars = get_stars(repo_stats)
        
        # Print Results
        print(f"{repo}: {stars} stars")

@task
def fetch_stats(github_repo: str):
    """
    Fetch the statistics for a GitHub repo
    """
    return httpx.get(f"https://api.github.com/repos/{github_repo}").json()

@task
def get_stars(repo_stats: dict):
    """
    Get the number of stars from GitHub repo statistics
    """
    return repo_stats['stargazers_count']

if __name__ == "__main__":
    show_stars([
        "PrefectHQ/prefect",
        "pydantic/pydantic",
        "huggingface/transformers"
    ])