# GitHub Profile Language Analytics

A comprehensive tool to analyze language usage across all your GitHub repositories (public and private) with detailed leaderboards.

## Features

- Analyzes all repositories owned by you (both public and private)
- Multiple visualization types with **modern, sleek design**:
  - **Leaderboard**: Horizontal bars with badges and repo breakdowns
  - **Bar Charts**: Vertical and horizontal bar charts with icons
  - **Pie/Donut Charts**: Circular visualizations with badge legends
- Three metric types for each visualization:
  - By Repository Count: How many repos use each language
  - By Lines of Code: Total lines written in each language
  - By Weighted Score: Equal weighting of repo count and line count
- **Modern visual styling**:
  - Subtle drop shadows and depth effects
  - Clean, minimalist design with professional typography
  - Language badge icons integrated into all chart types
  - Smooth gradients and polished aesthetics
  - High contrast, readable text with stroke outlines
- CLI arguments for flexible chart generation
- Excludes specified repositories via configuration
- Option to exclude forked repositories
- Filter out specific languages (defaults: HTML, CSS)
- Privacy option to hide/aggregate private repository names in visualizations
- Generates high-quality PNG visualizations (300 DPI)
- Badge images are cached locally for faster subsequent runs
- Supports 118+ programming languages with custom colors and logos

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create GitHub Personal Access Token:
   - Go to GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)
   - Generate new token with `repo` scope (to access private repos)
   - Copy the token

3. Configure the tool:

```bash
cp config.example.json config.json
```

Edit `config.json` and add:

- Your GitHub token
- Any repositories you want to exclude (optional)

## Usage

### Basic Usage

Run the analysis with default settings (leaderboard style):

```bash
python main.py
```

### CLI Options

```bash
python main.py --types leaderboard bar pie donut --output my_output
```

**Available Options:**

- `--types`: Visualization types to generate (can specify multiple)
  - `leaderboard`: Horizontal bars with language badges and repo breakdowns (default)
  - `bar`: Vertical bar charts (top 15 languages)
  - `horizontal-bar`: Simple horizontal bars without badges (top 20 languages)
  - `pie`: Pie charts (top 10 languages + "Other")
  - `donut`: Donut charts (top 10 languages + "Other")

- `--config`: Path to config file (default: `config.json`)

- `--output`: Output directory for visualizations (default: `output`)

### Examples

Generate all visualization types:

```bash
python main.py --types leaderboard bar horizontal-bar pie donut
```

Generate only pie and donut charts:

```bash
python main.py --types pie donut
```

Use custom config and output directory:

```bash
python main.py --config my_config.json --output my_charts
```

### Output Files

The tool generates files based on selected visualization types:

**Leaderboard** (with badges):

- `leaderboard_by_repos.png` - Sorted by repository count
- `leaderboard_by_lines.png` - Sorted by lines of code (with top 5 contributing repos)
- `leaderboard_by_weighted.png` - Sorted by weighted score

**Vertical Bar Charts**:

- `bar_by_repos.png`
- `bar_by_lines.png`
- `bar_by_weighted.png`

**Horizontal Bar Charts**:

- `horizontal_bar_by_repos.png`
- `horizontal_bar_by_lines.png`
- `horizontal_bar_by_weighted.png`

**Pie Charts**:

- `pie_by_repos.png`
- `pie_by_lines.png`
- `pie_by_weighted.png`

**Donut Charts**:

- `donut_by_repos.png`
- `donut_by_lines.png`
- `donut_by_weighted.png`

## Configuration

Example `config.json`:

```json
{
  "github_token": "ghp_your_token_here",
  "excluded_repos": ["test-repo", "old-project"],
  "include_forks": false,
  "excluded_languages": ["HTML", "CSS"],
  "hide_private_repo_names": false
}
```

Configuration options:

- `github_token`: Your GitHub Personal Access Token (required)
- `excluded_repos`: List of repository names to exclude from analysis (optional)
- `include_forks`: Set to `true` to include forked repositories, `false` to exclude them (default: false)
- `excluded_languages`: List of languages to exclude from analysis (default: ["HTML", "CSS"])
- `hide_private_repo_names`: Set to `true` to aggregate private repos as "[N Private Repos]" in breakdown visualizations (default: false)

## Language Configuration

The tool uses `languages.json` to configure language colors and badge icons for 100+ programming languages. This file contains:

- `color`: GitHub-style language color (hex format)
- `badge_color`: Color for shields.io badges (hex without #)
- `logo`: Simple Icons slug for the language logo (optional)

**Extending language support:**
To add or customize a language, edit `languages.json`:

```json
{
  "YourLanguage": {
    "color": "#FF5733",
    "badge_color": "FF5733",
    "logo": "yourlanguage"
  }
}
```

Languages not in the config will automatically use a fallback gray badge with the language name.

## How It Works

- **Repository Count**: Counts how many repositories use each language
- **Lines of Code**: Sums up the total lines of code per language across all repos
- **Weighted Score**: Normalizes both metrics (0-1 scale) and averages them for balanced ranking

## Output

All visualizations are saved as high-resolution PNGs (300 DPI) with modern, polished styling:

- **Color-coded visualizations** matching GitHub's language colors
- **Language badge icons** integrated into all chart types (not just leaderboards!)
- **Formatted numbers** (K/M notation for large values)
- **Chart-specific features**:
  - **Leaderboards**: Include badges and top contributing repos breakdown (top 5 repos per language)
  - **Bar Charts**: Badges below vertical bars or on y-axis for horizontal (top 15-20 languages)
  - **Pie/Donut Charts**: Badge legend on the right side (top 10 languages + "Other")
- Perfect for portfolios, presentations, and README files
