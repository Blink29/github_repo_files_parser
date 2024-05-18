from github_repo_files_parser import GitHubRepoFilesParser

parser = GitHubRepoFilesParser()

repo_url = "https://github.com/Blink29/image-compression-autoencoder"
parser.get_raw_repo_links(repo_url)