
from setuptools import setup, find_packages
import sys
import os
import codecs
import requests

name = input('your name')
print('hello,', name)


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


packages = find_packages(exclude=['tests*'])
requirements = requirements()

UPSTREAM_URLLIB3_FLAG = '--with-upstream-urllib3'
if UPSTREAM_URLLIB3_FLAG in sys.argv:
    sys.argv.remove(UPSTREAM_URLLIB3_FLAG)
    requirements.append('urllib3 >= 1.19.1')
    packages = [x for x in packages if not x.startswith(
        'telegram.vendor.ptb_urllib3')]

with codecs.open('README.rst', 'r', 'utf-8') as fd:
    fn = os.path.join('telegram', 'version.py')
    with open(fn) as fh:
        code = compile(fh.read(), fn, 'exec')
        exec(code)

    setup(name='python-telegram-bot',
        version
