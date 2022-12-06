"""Setup file for phatgpt."""
from setuptools import setup

long_description = """
Terminal based interface for chatgpt. I have attempted to mimic
the playgrounds current implementation as closely as possible. in order to use
the script you will need an api key for chatgpt.

You can get a key here https://openai.com/api/

set your api key to the enviroment variable OPENAI_API_KEY
"""

REQUIREMENTS = ['openai', 'python-dotenv']

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Utilities',
    'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    'Programming Language :: Python :: 3.10',
    'Environment :: Console',
    'Natural Language :: English'
]

setup(
    name='phatgpt',
    version='0.0.6',
    description='A simple terminal interface for chatgpt',
    long_description=long_description,
    url='https://github.com/th3r00t/phatgpt',
    author='th3r00t',
    author_email='admin@mylt.dev',
    license='GPL3',
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords='chatgpt ai',
    scripts=['bin/phatgpt']
)
