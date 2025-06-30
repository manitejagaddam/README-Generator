import requests
import json
import os

def save_repo_data_to_json(repositories_data, username, repo_name, filename='Data/repo_structure.json'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    print("✅ Saving full repo structure...")

    # Save full raw repo structure
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(repositories_data, json_file, indent=4)
    print("✅ Raw repo structure saved.")

    # Load and clean structure to keep only paths
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if "tree" in data:
        cleaned_tree = [{"path": item["path"]} for item in data["tree"] if "path" in item]

        cleaned_data = {
            "author": username,
            "repo_name": repo_name,
            "tree": cleaned_tree
        }

        with open('Data/data_cleaned.json', 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, indent=2)
        print("✅ Cleaned repo structure saved to Data/data_cleaned.json")
    else:
        print("❌ 'tree' key not found in response. Here's the data:", data)

def data_fetcher(username, project_name):
    base_url = f'https://api.github.com/repos/{username}/{project_name}/git/trees/main?recursive=1'

    print(f"🌐 Fetching repo structure from: {base_url}")
    response = requests.get(base_url)

    if response.status_code == 200:
        repos = response.json()
        save_repo_data_to_json(repos, username, project_name)
    else:
        print(f"❌ Failed to fetch repository tree. Status code: {response.status_code}")
        print(f"🔍 Error message: {response.text}")
