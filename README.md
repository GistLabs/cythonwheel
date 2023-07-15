# cythonwheel
How to create Github releases with cython

> 1. Create your account in [pypi.org](https://pypi.org/)
> 1. Move to build.yml in workflows directory
> 1. Change the username to yours in Upload manylinux wheel
```
    - name: Upload manylinux wheel
        run: |
          python -m twine upload -u ** your account ** -p ** your password **wheelhouse/*
```
