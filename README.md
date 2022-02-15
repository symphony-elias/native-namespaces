To create the tarballs, run:

```shell
python3 -m pip install build 
cd pkg_a
python -m build --sdist
twine upload -r testpypi dist/*
cd ../pkg_b
python -m build --sdist
twine upload -r testpypi dist/*
```