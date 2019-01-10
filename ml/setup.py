"""
# setup module
"""

import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

BASE = 'ml' if os.path.isdir(os.path.join(HERE, 'ml')) else ''

PREQ = os.path.join(HERE, BASE, "requirements.txt")
PREQ_DEV = os.path.join(HERE, BASE, "requirements-dev.txt")

setup(
    name='ml',
    version='0.0.1',
    description='Python Machine Learning Practice',
    long_description=README,
    classifiers=["Programming Language :: Python",
                 "Topic :: Machine Learning"],
    author='Jinchi Zhang',
    author_email='jizjiz148148@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[i.strip() for i in open(PREQ).readlines()],
    tests_require=[i.strip() for i in open(PREQ_DEV).readlines()],
    test_suite="ml",
    entry_points="""\
    [paste.app_factory]
    main = ml:main
    """,
)
