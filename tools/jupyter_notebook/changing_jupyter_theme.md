# Changing themes of jupyter notebook

## Install **jupyterthemes**

* `conda install -c conda-forge jupyterthemes` or `pip install jupyterthemes`

After we install **jupyterthemes**, we need to restart the jupyter notebook.

## List themes and change

* `jt --help`
* `jt -l` - List available themes
* `jt -t <theme_name>` - Install a particular theme. I prefer `jt -t onedork`
* `jt -r` - Reset to default theme
* `jt -t onedork -cellw 100% -lineh 170` - Changes the theme, sets the cell width to 100%.
