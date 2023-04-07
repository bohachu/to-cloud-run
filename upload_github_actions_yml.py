import argparse
import base64
import os

import requests
from dotenv import load_dotenv


def upload_github_actions_yml(file, content, repo, token, branch, path, name):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    repo_api_url = f"https://api.github.com/repos/{repo}"
    file_path = os.path.join(path, name)
    file_url = f"{repo_api_url}/contents/{file_path}"

    if file:
        with open(file, 'r') as f:
            content = f.read()

    if not content:
        raise ValueError("You must provide a valid .yml file or content.")

    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    file_response = requests.get(file_url, headers=headers)
    print("file_response", file_response.text)

    file_exists = file_response.status_code != 404
    file_data = file_response.json() if file_exists else {}

    update_data = {
        "message": f"Update {name}",
        "content": encoded_content,
        "branch": branch,
    }

    if "sha" in file_data:
        update_data["sha"] = file_data["sha"]

    response = requests.put(file_url, json=update_data, headers=headers)
    print("response", response.text)
    response.raise_for_status()

    print(f"Successfully uploaded {name} to {repo}/{branch}/{file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a GitHub Actions .yml file to a repository.")
    parser.add_argument("--file", "-f", help="Path to the .yml file.")
    parser.add_argument("--content", "-c", help="Content of the .yml file as a string.")
    parser.add_argument("--repo", "-r", required=True, help="GitHub repository, format: 'user/repo'.")
    parser.add_argument("--token", "-t", help="GitHub personal access token.")
    parser.add_argument("--branch", "-b", default="main", help="Branch to upload the .yml file (default: 'main').")
    parser.add_argument("--path", "-p", default=".github/workflows",
                        help="Path to store the .yml file in the repository (default: '.github/workflows').")
    parser.add_argument("--name", "-n", required=True, help="Name of the .yml file in the repository.")
    args = parser.parse_args()

    load_dotenv()
    token = args.token or os.getenv("GITHUB_ACCESS_TOKEN")
    if not token:
        raise ValueError("You must provide a valid GitHub token.")

    upload_yml(args.file, args.content, args.repo, token, args.branch, args.path, args.name)
