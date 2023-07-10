from setuptools import setup
from Cython.Build import cythonize
from setuptools.dist import Distribution
import tomllib


with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False


setup(
    name=data['tool']['poetry']['name'],
    version=data['tool']['poetry']['version'],
    author=data['tool']['poetry']['authors'][0].split()[0],
    author_email=data['tool']['poetry']['authors'][0].split()[1],
    url='https://gistlabs.com',
    install_requires=['numpy'],
    ext_modules=cythonize(
        "cythonwheel/**/*.py",
        compiler_directives={'language_level': 3, "linetrace": False},
    ),
    include_package_data=True,
    distclass=BinaryDistribution,
)
