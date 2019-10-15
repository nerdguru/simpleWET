import setuptools

setuptools.setup(
    name="simpleWET",
    version="0.0.1",
    description="A simple WebEx Teams package",
    url="https://github.com/nerdguru/simpleWET",
    packages=setuptools.find_packages(),
    install_requires=[
       'requests'
    ],
)
