#! /bin/bash

set -xeuo pipefail

# BUMP_VERSION=$1
# if [ "$BUMP_VERSION" = "" ]
# then
BUMP_VERSION="patch"
# fi

bumpversion $BUMP_VERSION
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
git push --tags
git push origin "$CURRENT_BRANCH:$CURRENT_BRANCH"

rm -rf dist/
python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*
