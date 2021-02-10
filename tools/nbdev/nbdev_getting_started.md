# Getting started with nbdev

## nbdev features

* Notebooks to python modules
* Convert notebooks to python package and publish to pypi
* IDE like usage.
* Documentation can also be built for the generated package.

## Setting up nbdev

* `pip install nbdev` or `poetry add nbdev --dev`
* Clone the [nbdev repository](https://github.com/fastai/nbdev_template)
* Edit the **settings.ini** with the required details like library name, user name, author, description etc.
* Execute `nbdev_install_git_hooks` to set up the git hooks.
* Executing `nbdev_build_lib` produces python modules from jupyter notebooks and `nbdev_build_docs` generates the documentation.
* `index.ipynb` is filled with details about the package. This gets converted to the package **README.md** when building the documentation.
* By placing this snippet as the last cell `from nbdev.export import notebook2script` we can convert the notebook to python module.
* `nbdev_test_nbs` command can be used to run the tests in paralle.

## Programming using nbdev

> nbdev uses special comments, or flags, as a markup language that allows you to control various aspects of the docs and how code is exported to modules, and how code is tested. [nbdev minimal example](https://nbdev.fast.ai/example.html)

* First cell of the notebook must include `#default_exp module_name`.
* `#export` - Export the code in the current cell to the python module
* `#exports` -
* `#hide` - Hide the cell when generating the docs

* Autoreload the changes from modules of other notebooks can be done by adding the following snippet on top of your current working notebook

```Python
%load_ext autoreload
%autoreload 2
```

* Cells containing `assert` statements automatically become tests.
* Within the notebook, documentation can be viewed using `show_doc(class_func_mehtod)`

---

## References

* [nbdev tutorial](https://nbdev.fast.ai/tutorial.html)
* [A Step-by-Step Introduction to Starting nbdev — Exploratory Programming](https://towardsdatascience.com/a-step-by-step-introduction-to-starting-nbdev-exploratory-programming-4a761ed1f796)
* [The point of no return: Using nbdev](https://towardsdatascience.com/the-point-of-no-return-using-nbdev-for-the-past-6-months-changed-the-way-i-code-in-jupyter-2c5b0e6d2c4a)
