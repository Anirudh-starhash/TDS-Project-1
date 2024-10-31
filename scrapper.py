import os
import requests
import pandas as pd
import time

GITHUB_API_BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {os.getenv('GITHUB_PAT')}"
}

# Helper function to handle GitHub API rate limits
def handle_rate_limits(response):
    if response.status_code == 403 and "X-RateLimit-Remaining" in response.headers:
        if int(response.headers["X-RateLimit-Remaining"]) == 0:
            reset_time = int(response.headers["X-RateLimit-Reset"])
            wait_time = reset_time - int(time.time())
            print(f"Rate limit exceeded, waiting for {wait_time} seconds.")
            time.sleep(wait_time)
            return True
    return False

# Function to get users in Sydney with over 100 followers
def get_sydney_users(min_followers=100):
    users = []
    page = 1
    while True:
        query = f"location:Sydney followers:>{min_followers}"
        url = f"{GITHUB_API_BASE_URL}/search/users?q={query}&page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        
        if handle_rate_limits(response):
            continue

        if response.status_code != 200:
            print(f"Error fetching users: {response.status_code}, {response.text}")
            break

        data = response.json()
        if "items" in data:
            users.extend(data["items"])
            if len(data["items"]) < 100:
                break
        else:
            break
        page += 1
    return users

# Function to get detailed information about a user
def get_user_details(username):
    url = f"{GITHUB_API_BASE_URL}/users/{username}"
    response = requests.get(url, headers=HEADERS)
    
    if handle_rate_limits(response):
        return get_user_details(username)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user details for {username}: {response.status_code}, {response.text}")
        return {}

# Function to clean company name
def clean_company_name(company):
    if company:
        company = company.strip()
        if company.startswith('@'):
            company = company[1:]
        return company.upper()
    return ""

# Function to get repositories of a user
def get_user_repo(username, max_repos=500):
    repos = []
    page = 1
    while True:
        url = f"{GITHUB_API_BASE_URL}/users/{username}/repos?page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        
        if handle_rate_limits(response):
            continue
        
        if response.status_code != 200:
            print(f"Error fetching repositories for {username}: {response.status_code}, {response.text}")
            break
        
        data = response.json()
        repos.extend(data)
        if len(data) < 100 or len(repos) >= max_repos:
            break
        page += 1
    return repos[:max_repos]

# Function to save users data to CSV
def save_users_to_csv(user_data, filename="users.csv"):
    if user_data:
        users_df = pd.DataFrame(user_data)
        users_df.to_csv(filename, index=False)
        print(f"Saved {len(user_data)} users to {filename}")
    else:
        print("No user data to save.")

# Function to save repositories data to CSV
def save_repositories_to_csv(repos_data, filename="repositories.csv"):
    if repos_data:
        repos_df = pd.DataFrame(repos_data)
        repos_df.to_csv(filename, index=False)
        print(f"Saved {len(repos_data)} repositories to {filename}")
    else:
        print("No repository data to save.")

# Main function
def main():
    users = get_sydney_users()
    users_data = []
    repos_data = []
    
    for user in users:
        username = user['login']
        user_details = get_user_details(username)
        
        # Add user data to the list
        users_data.append({
            'login': user_details.get('login', ''),
            'name': user_details.get('name', ''),
            'company': clean_company_name(user_details.get('company', '')),
            'location': user_details.get('location', ''),
            'email': user_details.get('email', ''),
            'hireable': user_details.get('hireable', ''),
            'bio': user_details.get('bio', ''),
            'public_repos': user_details.get('public_repos', 0),
            'followers': user_details.get('followers', 0),
            'following': user_details.get('following', 0),
            'created_at': user_details.get('created_at', '')
        })
        
        print("Adding")
        
        # Fetch and add repository data to the list
        repos = get_user_repo(username)
        for repo in repos:
            if isinstance(repo, dict):  # Ensure repo is a dictionary
                repos_data.append({
                    'login': username,
                    'full_name': repo.get('full_name', ''),
                    'created_at': repo.get('created_at', ''),
                    'stargazers_count': repo.get('stargazers_count', 0),
                    'watchers_count': repo.get('watchers_count', 0),
                    'language': repo.get('language', ''),
                    'has_projects': repo.get('has_projects', False),
                    'has_wiki': repo.get('has_wiki', False),
                    'license_name': repo.get('license', {}).get('key', '') if repo.get('license') else ''
                })
                print('Adding')
            else:
                print(f"Unexpected format for repository data: {repo}")
    
    # Save data to CSV files
    save_users_to_csv(users_data, "users.csv")
    save_repositories_to_csv(repos_data, "repositories.csv")

if __name__ == '__main__':
    main()
