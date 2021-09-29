import requests


def request(url: str):
    res = requests.get(url)
    return res.json()


def get_repositories(user: str):
    url = f'https://api.github.com/users/{user}/repos'
    return request(url)


def get_commits(user: str, repo: str):
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    return request(url)


def main():
    user = 'jjzcru'
    for repository in get_repositories(user):
        repo = repository['name']
        total = len(get_commits(user, repo))
        print(f"Repo: {repo} Number of commits: {total}")


main()
