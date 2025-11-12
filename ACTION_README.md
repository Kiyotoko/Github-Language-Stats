# GitHub Profile Language Analytics Action

Automatically generate visualizations of your programming language usage across all your GitHub repositories.

## Why This Action?

Unlike other tools that show only your top 6 languages, this action:
- Analyzes ALL your languages, not just the top 6
- Works with both public and private repositories
- Highly configurable to match your needs
- Generates multiple visualization types with modern design

## Setup

### 1. Create a Personal Access Token

The action requires a Personal Access Token (PAT) to access your repositories.

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name: `Language Stats`
4. Select scope: `repo` (Full control of private repositories)
5. Click "Generate token" and copy it

### 2. Add Token as Secret

1. Go to your repository Settings
2. Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `STATS_TOKEN`
5. Value: Paste your PAT
6. Click "Add secret"

### 3. Create Workflow

Create `.github/workflows/stats.yml`:

```yaml
name: Update Language Statistics

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

permissions:
  contents: write

jobs:
  update-stats:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: stefvuck/github-profile-language-analytics@v1
        with:
          github_token: ${{ secrets.STATS_TOKEN }}
          visualization_types: 'leaderboard'
          output_path: 'stats'
```

### 4. Add to README

```markdown
![Language Stats](stats/leaderboard_by_lines.png)
```

## Configuration

| Input | Description | Default |
|-------|-------------|---------|
| `github_token` | Personal Access Token with `repo` scope | Required |
| `visualization_types` | Types to generate | `leaderboard bar pie` |
| `output_path` | Output directory | `github-stats` |
| `exclude_repos` | Comma-separated repos to skip | `''` |
| `include_forks` | Include forked repos | `false` |
| `exclude_languages` | Comma-separated languages to skip | `HTML,CSS` |
| `top_repos_count` | Repos shown in leaderboard | `5` |
| `commit_message` | Git commit message | `Update language statistics` |
| `dark_mode` | Enable dark mode theme | `false` |

## Visualization Types

- `leaderboard` - Horizontal bars with badges and top contributing repos
- `bar` - Vertical bars (top 12 languages)
- `horizontal-bar` - Horizontal bars (top 15 languages)
- `pie` - Pie chart (top 8 + "Other")
- `donut` - Donut chart (top 8 + "Other")

## Output Files

Each type generates 3 files:
- `*_by_repos.png` - Sorted by repository count
- `*_by_lines.png` - Sorted by lines of code
- `*_by_weighted.png` - Balanced ranking

## Advanced Configuration

```yaml
- uses: stefvuck/github-profile-language-analytics@v1
  with:
    github_token: ${{ secrets.STATS_TOKEN }}
    visualization_types: 'leaderboard bar pie donut'
    output_path: 'language-stats'
    exclude_repos: 'test-repo,old-project'
    include_forks: 'true'
    exclude_languages: 'HTML,CSS,Markdown'
    top_repos_count: '10'
    dark_mode: 'true'
```

## Troubleshooting

### 403 Forbidden Error

If you see `Resource not accessible by integration`, your token doesn't have the required permissions.

**Solution**: Create a Personal Access Token with `repo` scope (see Setup above).

### Images Not Committing

Ensure your workflow has `contents: write` permission and the output directory is not in `.gitignore`.

## Local Development

```bash
pip install -r requirements.txt
cp config.example.json config.json
# Edit config.json with your token
python main.py --types leaderboard bar pie --dark-mode
```

## License

MIT
