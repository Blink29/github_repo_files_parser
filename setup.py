from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="github_repo_files_parser",
    version="1.0.0",
    description="Extract file paths from GitHub repositories categorized by extension",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Paurush Kumar",
    packages=["github_repo_files_parser"],
    zip_safe=False,
    # project_urls={
    #     "Documentation": "https://pypi.org/project/webscapy/",
    #     "Source": "https://pypi.org/project/webscapy/",
    # },
    install_requires=[ "Github" ]
)