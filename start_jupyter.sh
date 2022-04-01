#!/bin/bash

poetry run jupyter notebook \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8889 \
  --NotebookApp.port_retries=0 \
  --VoilaConfiguration.enable_nbextensions=True
