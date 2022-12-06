"""Setup file for phatgpt."""
from setuptools import setup

with open("DESCRIPTION.txt") as file:
    long_description = file.read()

REQUIREMENTS = ['openai', 'python-dotenv']

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Utilities',
    'License :: OSI Approved :: GNU General Public License v3 or later (GLPv3+)',
    'Programming Language :: Python :: 3.10',
    'Enviroment :: Console',
    'Natural Language :: English'
]

setup(
    name='phatgpt',
    version='0.0.1',
    description='A simple terminal interface for chatgpt',
    long_description=long_description,
    url='https://github.com/th3r00t/phatgpt',
    author='th3r00t',
    author_email='admin@mylt.dev',
    license='GPL3',
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords='chatgpt ai'
)
