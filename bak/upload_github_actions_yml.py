import argparse
import os

from upload_files_to_github import upload_files_to_github
from dotenv import load_dotenv


def upload_github_actions_yml(files, file_content, repo, token, branch="main", path=".github/workflows", name="workflow.yml"):
    if not files and not file_content:
        raise ValueError("You must provide at least one file or directory path or file content.")

    if files and file_content:
        raise ValueError("You can only provide either a file or directory path or file content, not both.")

    file_paths = [os.path.join(path, file) if os.path.isdir(file) else file for file in files]

    if file_content:
        file_paths = [os.path.join(path, name)]
        with open(file_paths[0], "w") as f:
            f.write(file_content)

    upload_files_to_github(file_paths, repo, token, branch)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a GitHub Actions .yml file to a repository.")
    parser.add_argument("--file", "-f", help="Path to the .yml file.")
    parser.add_argument("--content", "-c", help="Content of the .yml file as a string.")
    parser.add_argument("--repo", "-r", required=True, help="GitHub repository, format: 'user/repo'.")
    parser.add_argument("--token", "-t", help="GitHub personal access token.")
    parser.add_argument("--branch", "-b", default="main", help="Branch to upload the files (default: 'main').")
    parser.add_argument("--path", "-p", default=".github/workflows",
                        help="Path to store the files in the repository (default: '.github/workflows').")
    parser.add_argument("--name", "-n", default="workflow.yml", help="Name of the file in the repository.")
    args = parser.parse_args()

    load_dotenv()
    token = args.token or os.getenv("GITHUB_ACCESS_TOKEN")
    if not token:
        raise ValueError("You must provide a valid GitHub token.")

    upload_github_actions_yml(args.file, args.content, args.repo, token, args.branch, args.path, args.name)