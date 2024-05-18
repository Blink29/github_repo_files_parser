# GitHub Repository Parser

Hosted on [github.com/Blink29](https://github.com/Blink29)

Why parse a repository?
<ul>
<li>To collect all files of a particular repository, flattened and grouped by extension, is too menial to be done manually. 
<li>Grouped files can be used for further analysis / use / testing, based on requirements.
</ul>

How does the parser work?
<ul>
<li>The parser is developed using the GitHub API.</li>
<li>Recursive level-wise file parsing is done to obtain absolute path of each file in the repository.</li> 
<li>Simultaneously, files of each type are grouped together and a dictionary of type { extension: array_of_files } is returned.</li>
</ul>

<h2>Installation</h2>
<code>pip install github-repo-files-parser==1.0.0</code>


<h2>Illustration</h2>

```jsx
from github_repo_files_parser import GitHubRepoFilesParser

parser = GitHubRepoFilesParser()

repo_url = "https://github.com/Blink29/github_repo_files_parser"
parser.get_raw_repo_links(repo_url)
```

<h2>Sample Output</h2>

```yaml
{
  "py": [
    "https://github.com/Blink29/github_repo_files_parser/blob/main/index.py",
    "https://github.com/Blink29/github_repo_files_parser/blob/main/setup.py",
    "https://github.com/Blink29/github_repo_files_parser/blob/main/github_repo_files_parser/__init__.py",
    "https://github.com/Blink29/github_repo_files_parser/blob/main/github_repo_files_parser/github_repo_files_parser.py"
  ],
  "md": [
    "https://github.com/Blink29/github_repo_files_parser/blob/main/README.md"
  ],
  "gitignore": [
    "https://github.com/Blink29/github_repo_files_parser/blob/main/.gitignore"
  ],
  "directories": [
    "https://github.com/Blink29/github_repo_files_parser/tree/main/github_repo_files_parser"
  ],
  "cfg": [
    "https://github.com/Blink29/github_repo_files_parser/blob/main/github_repo_files_parser/setup.cfg"
  ]
}
```