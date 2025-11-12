from typing import List, Dict, Optional

from github import Github
from github.GithubException import GithubException


class GitHubClient:
    def __init__(self, token: str):
        self.github = Github(token)
        self.token = token
        self.user = self.github.get_user()

    def is_repo_private(self, repo) -> bool:
        return repo.private

    def get_all_repos(self, excluded_repos: Optional[List[str]] = None,
                      include_forks: bool = False) -> List:
        excluded_repos = excluded_repos or []
        repos = []

        for repo in self.user.get_repos(affiliation='owner'):
            if repo.name not in excluded_repos:
                if include_forks or not repo.fork:
                    repos.append(repo)

        return repos

    def get_language_stats(self, repo) -> Dict[str, int]:
        try:
            return repo.get_languages()
        except GithubException as e:
            print(f"Error fetching languages for {repo.name}: {e}")
            return {}

    def get_username(self) -> str:
        return self.user.login
