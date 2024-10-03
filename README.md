
# GitHub Insights Dashboard

A Python-based dashboard that retrieves insights (Stars, Forks, Pull Requests, Issues) from GitHub repositories using the GitHub GraphQL API.

## Features
- Fetches repository insights using GitHub's GraphQL API.
- Visualizes repository data using bar charts with `matplotlib`.
- Lists key metrics like stars, forks, pull requests, and issues.

## Getting Started

### Prerequisites
To run this project, you'll need:
- Python 3.x
- A GitHub Personal Access Token (PAT) with the necessary permissions.
- The following Python libraries:
  - `requests`
  - `pandas`
  - `matplotlib`

You can install the required libraries by running:
```bash
pip install -r requirements.txt
```

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/github-insights-dashboard.git
   ```

2. Navigate to the project folder:
   ```bash
   cd github-insights-dashboard
   ```

3. Replace the `GITHUB_TOKEN` in the Python script with your own GitHub Personal Access Token.

4. Run the script:
   ```bash
   python main.py
   ```

### Usage

- This script fetches repository data such as:
  - Stargazers (Stars)
  - Forks
  - Pull Requests
  - Issues
- The data is visualized using a bar chart.


