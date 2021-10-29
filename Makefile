install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt --user

lint:
	python -m pylint --disable=R,C cli.py test_cli.py app.py

format:
	python -m black *.py

test:
	python -m pytest -vv -cov=cli test_cli.py