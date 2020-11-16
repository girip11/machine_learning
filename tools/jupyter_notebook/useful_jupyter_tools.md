# Useful jupyter notebook tools and extensions

## Notebook diff using nbdime

* To compare the diff between the notebooks, use [nbdime](https://nbdime.readthedocs.io/en/latest/).

## Running QA tools on notebook using nbQA

* [nbqa](https://nbqa.readthedocs.io/en/latest/) can be used to run quality assurance tools like flake8, pylint, mypy on notebooks.

## Changing themes of jupyter notebook using **jupyterthemes**

* `conda install -c conda-forge jupyterthemes` or `pip install jupyterthemes`

After we install **jupyterthemes**, we need to restart the jupyter notebook.

## List themes and change

* `jt --help`
* `jt -l` - List available themes
* `jt -t <theme_name>` - Install a particular theme. I prefer `jt -t onedork`
* `jt -r` - Reset to default theme
* `jt -t onedork -cellw 100% -lineh 170` - Changes the theme, sets the cell width to 100%.
