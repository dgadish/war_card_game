isort -c .
black -c .
pylint -rn -sn .
mypy .
