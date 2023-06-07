# Packaging with python

From [here](https://pybit.es/articles/how-to-package-and-deploy-cli-apps/)

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
say_hello
```

Get rid of it:

```
pip uninstall hello
```
