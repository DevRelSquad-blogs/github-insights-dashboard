import requests
import pandas as pd
import matplotlib.pyplot as plt

# GitHub Personal Access Token (Ensure to keep it secure)
GITHUB_TOKEN = 'Your_github_token'
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

# GraphQL query to get repository data
def run_query(query): 
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed with status code {request.status_code}. {request.text}")

# Query to fetch repository insights
query = """
{
  viewer {
    repositories(first: 10) {
      nodes {
        name
        stargazerCount
        forkCount
        pullRequests {
          totalCount
        }
        issues {
          totalCount
        }
      }
    }
  }
}
"""

# Run the query
result = run_query(query)

# Process the data
repos_data = []
for repo in result['data']['viewer']['repositories']['nodes']:
    repos_data.append({
        'Repository': repo['name'],
        'Stars': repo['stargazerCount'],
        'Forks': repo['forkCount'],
        'Pull Requests': repo['pullRequests']['totalCount'],
        'Issues': repo['issues']['totalCount']
    })

# Convert to pandas DataFrame for easy manipulation
df = pd.DataFrame(repos_data)
print(df)

# Plot the data for visualization
df.set_index('Repository', inplace=True)
df.plot(kind='bar', figsize=(10, 6), title="GitHub Repositories Insights")
plt.ylabel('Count')
plt.tight_layout()
plt.show()
