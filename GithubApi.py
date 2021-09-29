import requests
from typing import Any, List, Dict


def request(url: str) -> Dict:
    # Return a response from a request as a json object
    res = requests.get(url)
    return res.json()


def get_repositories(user: str) -> List[Dict]:
    # Return a list of repositories from a user
    url = f"https://api.github.com/users/{user}/repos"
    return request(url)


def get_commits(user: str, repo: str) -> List[Dict]:
    # Return a list of repositories from a user
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    return request(url)


def main() -> None:
    user = 'jjzcru'
    for repository in get_repositories(user):
        repo = repository['name']
        total = len(get_commits(user, repo))
        print(f"Repo: {repo} Number of commits: {total}")


if __name__ == "__main__":
    main()
