# Setting up voila

```bash
pipenv install voila
jupyter serverextension enable voila --sys-prefix
```

After enabling voila, I had the issue where the ipywidgets were not rendering properly. So I went to `$HOME/.local/jupyter` and I executed the following commands.

```Bash
rm -fr $HOME/.local/jupyter/kernels
rm -fr $HOME/.local/jupyter/nbconvert/templates
```

The `$HOME` path was taking higher precedence than those paths present in the virtual environment. After this, ipywidgets are rendering as expected.

To start voila as jupyter extension use the following command

```bash
# You might need to install another jupyter extension called 
# jupyter_http_over_ws for the below command to work
# checkout the markdown "./connect_colab_to_local_jupyter.md"
jupyter notebook \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8889 \
  --NotebookApp.port_retries=0 \
  --VoilaConfiguration.enable_nbextensions=True
```

To start voila server separately from jupyter server, use the following command

```Bash
# use --debug to debug if something is not working
voila fastai_deep_learning_book/2_model_to_production/voila_test_app.ipynb --enable_nbextensions=True
```

## References

* [Voila as jupyter server extension](https://voila.readthedocs.io/en/stable/using.html#as-a-jupyter-server-extension)
* [Voila](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93)
