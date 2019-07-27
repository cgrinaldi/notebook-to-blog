import os
import github
from github import Github
from dotenv import load_dotenv
from loguru import logger


def create_gist(code, gh_cred_filepath):
    # gh_cred_path must include GITHUB_USER and GITHUB_PASSWORD
    load_dotenv(dotenv_path=gh_cred_filepath)

    user = os.getenv("GITHUB_USER")
    pw = os.getenv("GITHUB_PASSWORD")
    g = Github(user, pw)
    user = g.get_user()
    gist = user.create_gist(
        public=False, files={"notebook_gist.py": github.InputFileContent(code)}
    )
    logger.info(f"creating new gist with id={gist.id}")
    return gist.id
