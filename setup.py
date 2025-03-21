from setuptools import setup, find_packages

setup(
    name="bg_remover",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "rembg",
        "Pillow"
    ],

)
