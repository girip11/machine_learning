# Using notebooks from Github in Colab

## Tools

- [Open in Colab](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo) google chrome extension helps converting github notebook url to colab notebook url. This extension is from the colab-team

## Open github repo in colab

- When we are in the github repository page, we can use the chrome extension to open the notebook in the colab.

- If we dont have the extension installed, then we can manually fabricate the url using the below template.

```Python
# github url looks like
github_domain = "https://github.com"
notebook_path_in_github = "googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb"
github_notebook_url = f"{github_domain}/{notebook_path_in_github}"
print(github_notebook_url)

colab_domain = "https://colab.research.google.com"
colab_github_notebook_url = f"{colab_domain}/github/{notebook_path_in_github}"
print(colab_github_notebook_url)
```

## Opening private github repos from Colab

- Visiting `https://colab.research.google.com/github` will request for github permissions so that colab can access the user's github repository.
- Once colab is given permissions to access the user's github account, we can select a github repository from the list of user's repositories.
- The repository could be a private repository as well. Once we select a repository, then we can select a notebook to open in the colab.

**NOTE**: Free accounts right now can only have one active session running. If we have to open and run another notebook, then we need to terminate the session of the other notebook currently in use.

## Saving the changes back to github repo

- When opening a notebook from github, colab makes a copy of the notebook. So the source is not modified.
- But colab provides provisions to get the changes back to the github repository.
- From `File` menu we could save the changes back to github or to google drive.

## Using Git repositories with colab and google drive

- Suppose our notebook requires some assets present in the repository, then we could clone the git repository to the google drive by mounting it in the colab notebook session.

```Python
# mounting the google drive
from google.colab import drive
drive.mount("/content/gdrive")
```

- Within the notebook we can execute the following commands

```Bash
# install git if not already installed
# colab environment has git installed
!git --version

# check current directory
!pwd

%cd gdrive/My Drive/project_folder

! git clone <repo_url>
```

- ***

## References

- [Colab github demo](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=K-NVg7RjyeTk)

- [How to use Google Colaboratory to clone a GitHub Repository to your Google Drive?](https://medium.com/@ashwindesilva/how-to-use-google-colaboratory-to-clone-a-github-repository-e07cf8d3d22b)
