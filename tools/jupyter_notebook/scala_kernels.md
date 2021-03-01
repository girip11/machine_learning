# Scala kernels for Jupyter

## [Almond](https://github.com/almond-sh/almond)

* Follow the installation steps found [here](https://almond.sh/docs/quick-start-install)

## Apache Toree

* Toree 0.5 works with spark 3.0.0 and scala 2.12

```Bash
# change to latest release
poetry run pip install https://dist.apache.org/repos/dist/dev/incubator/toree/0.5.0-incubating-rc1/toree-pip/toree-0.5.0.tar.gz
poetry run jupyter toree install --user --kernel_name=toree --spark_home=/opt/spark
```
