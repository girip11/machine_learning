# Jupyter notebook quality check tools

[nbqa](https://github.com/nbQA-dev/nbQA) is a tool using which we can run the following tools on jupyter notebooks

* flake8
* black
* pytest
* isort
* mypy
* doctest

```Bash
pipenv run nbqa isort "$1"

pipenv run nbqa black "$1"

pipenv run nbqa flake8 "$1"

pipenv run nbqa mypy "$1"
```

* `.nbqa.ini` can be used to place the configuration for all these tools.
