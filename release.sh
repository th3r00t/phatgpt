#!/usr/bin/bash
rm -rf dist/*
python -m build .
# twine upload -r testpypi dist/* # Upload to testpypi
twine upload -r pypi dist/* # Upload to pypi
