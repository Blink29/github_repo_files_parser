import os
import shutil
import subprocess
import json

class GitHubRepoFilesParser:
    def __init__(self):
        self.rawUrls = {}

    def gather_raw_urls(self, repo_dir, owner, repo_name):
        print("Collecting files from the cloned repository.")
        for root, dirs, files in os.walk(repo_dir):
            if '.git' in dirs:
                dirs.remove('.git')
            for file in files:
                file_path = os.path.relpath(os.path.join(root, file), repo_dir)
                blob_url = f"https://github.com/{owner}/{repo_name}/blob/main/{file_path.replace(os.sep, '/')}"
                extension = file.split('.')[-1] if '.' in file else 'Miscellaneous'
                if extension in self.rawUrls:
                    self.rawUrls[extension].append(blob_url)
                else:
                    self.rawUrls[extension] = [blob_url]
            for dir in dirs:
                dir_path = os.path.relpath(os.path.join(root, dir), repo_dir)
                tree_url = f"https://github.com/{owner}/{repo_name}/tree/main/{dir_path.replace(os.sep, '/')}"
                if "directories" in self.rawUrls:
                    self.rawUrls["directories"].append(tree_url)
                else:
                    self.rawUrls["directories"] = [tree_url]

    def clone_repo(self, repo_url, repo_dir):
        subprocess.run(["git", "clone", repo_url, repo_dir], check=True)

    def delete_repo(self, repo_dir):
        shutil.rmtree(repo_dir)

    def get_raw_repo_links(self, repo_url):
        # Extract owner and repo name to form a unique directory name
        owner = repo_url.split('https://github.com/')[1].split('/')[0]
        repo_name = repo_url.split('https://github.com/')[1].split('/')[1]
        repo_dir = f"{owner}-{repo_name}"

        self.clone_repo(repo_url, repo_dir)
        self.gather_raw_urls(repo_dir, owner, repo_name)
        with open('urls.json', 'w') as f:
            json.dump(self.rawUrls, f)
        self.delete_repo(repo_dir)
        return self.rawUrls