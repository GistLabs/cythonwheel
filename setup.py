from setuptools import setup
from Cython.Build import cythonize
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False


setup(
    name="cythonwheel",
    version="0.2.0",
    url='https://gistlabs.com',
    install_requires=['numpy'],
    ext_modules=cythonize(
        "cythonwheel/**/*.py",
        compiler_directives={'language_level': 3, "linetrace": False},
    ),
    include_package_data=True,
    distclass=BinaryDistribution, )
