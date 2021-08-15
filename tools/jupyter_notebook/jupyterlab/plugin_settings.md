# Plugin settings

## Language server

```JSON
{
  "language_servers": {
    "pylsp": {
      "serverSettings": {
        "pylsp.configurationSources": ["flake8"],
        "pylsp.plugins.pydocstyle.enabled": true,
        "pylsp.plugins.yapf.enabled": false,
        "pylsp.plugins.autopep8.enabled": false,
        "pylsp.plugins.pyflakes.enabled": false,
        "pylsp.plugins.flake8.enabled": true,
        "pylsp.plugins.pylsp_mypy.enabled": true,
        "pylsp.plugins.pyls_isort.enabled": true,
        "pylsp.plugins.pylsp_black.enabled": true
      }
    }
  }
}
```

## Jupyter code formatter

```JSON
{
    "formatOnSave": true
}
```
