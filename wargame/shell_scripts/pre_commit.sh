pytest .
isort -c .
black -c .
pylint -rn -sn war_game
pylint -rn -sn tests
mypy .
