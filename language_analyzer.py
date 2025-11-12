from typing import Dict, List, Tuple, Optional
from collections import defaultdict


class LanguageAnalyzer:
    def __init__(self, excluded_languages: Optional[List[str]] = None,
                 hide_private_repo_names: bool = False):
        self.language_lines = defaultdict(int)
        self.language_repos = defaultdict(set)
        self.language_repo_lines = defaultdict(lambda: defaultdict(int))
        self.excluded_languages = set(excluded_languages or [])
        self.hide_private_repo_names = hide_private_repo_names
        self.private_repos = set()

    def add_repo_languages(self, repo_name: str, languages: Dict[str, int],
                          is_private: bool = False):
        if is_private:
            self.private_repos.add(repo_name)

        for language, lines in languages.items():
            if language not in self.excluded_languages:
                self.language_lines[language] += lines
                self.language_repos[language].add(repo_name)
                self.language_repo_lines[language][repo_name] = lines

    def get_by_repos(self) -> List[Tuple[str, int]]:
        result = list(self.language_repos.items())
        return sorted([(lang, len(repos)) for lang, repos in result],
                     key=lambda x: x[1], reverse=True)

    def get_by_lines(self) -> List[Tuple[str, int]]:
        result = list(self.language_lines.items())
        return sorted(result, key=lambda x: x[1], reverse=True)

    def get_by_weighted(self) -> List[Tuple[str, float]]:
        if not self.language_repos:
            return []

        max_repos = max(len(repos) for repos in self.language_repos.values())
        max_lines = max(self.language_lines.values()) if self.language_lines else 1

        weighted_scores = {}
        for language, repos in self.language_repos.items():
            repos_normalized = len(repos) / max_repos
            lines_normalized = self.language_lines[language] / max_lines
            weighted_scores[language] = (repos_normalized + lines_normalized) / 2

        result = list(weighted_scores.items())
        return sorted(result, key=lambda x: x[1], reverse=True)

    def get_all_languages(self) -> List[str]:
        return list(self.language_repos.keys())

    def get_top_contributing_repos(self, language: str,
                                   top_n: int = 10) -> List[Tuple[str, int]]:
        if language not in self.language_repo_lines:
            return []

        repo_lines = self.language_repo_lines[language]

        if not self.hide_private_repo_names:
            sorted_repos = sorted(repo_lines.items(), key=lambda x: x[1], reverse=True)
            return sorted_repos[:top_n]

        result = []
        private_total = 0
        private_count = 0

        for repo, lines in sorted(repo_lines.items(), key=lambda x: x[1], reverse=True):
            if repo in self.private_repos:
                private_total += lines
                private_count += 1
            else:
                result.append((repo, lines))

        if private_count > 0:
            result.append((f"[{private_count} Private Repos]", private_total))

        return sorted(result, key=lambda x: x[1], reverse=True)[:top_n]
