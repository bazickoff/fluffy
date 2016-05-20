from setuptools import find_packages
from setuptools import setup

setup(
    name='fluffy-server',
    version='0.0.1',
    author='Chris Kuehl',
    author_email='ckuehl@ocf.berkeley.edu',
    packages=find_packages(),
    install_requires={
        # TODO: upgrade this
        'django==1.6.1',
    },
    classifiers={
        'Programming Language :: Python :: 3',
    },
)