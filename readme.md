# Packaging with python

From [here](https://pybit.es/articles/how-to-package-and-deploy-cli-apps/)

Create a venv

```
python -m venv venv
```

Activate the venv

```
source venv/bin/activate.sh
```

Install stuff to build:

```
pip install build
```

Build it

```
python -m build
```

Install it:

```
pip install dist/hello-0.0.1-py3-none-any.whl
```

Use it:

```
cat_fact
```

Get rid of it:

```
pip uninstall hello
```
