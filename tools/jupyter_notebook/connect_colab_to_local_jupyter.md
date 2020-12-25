# Connect Colab notebook to local jupyter notebook

* Install **jupyter_http_over_ws** jupyter extension

```Bash
pipenv install jupyter_http_over_ws

# enable jupyter over websocket
# stop if any jupyter server is already running
jupyter serverextension enable --py jupyter_http_over_ws

# Launch the jupyter notebook using the follwing command
jupyter notebook \
       --NotebookApp.allow_origin='https://colab.research.google.com' \
       --port=8889 \
       --NotebookApp.port_retries=0
```

* After launching the local jupyter server, from colab webpage, select **connect to the local runtime** and copy the URL with token that would look something like `http://localhost:8889/?token=7dddc451a458d5b4a24f7c807a56da17a3e60dbd9ab8c549` and paste and select **connect**.
* Now the google colab notebook will run locally.
