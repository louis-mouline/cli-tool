install:
	pip install --upgrade pip --user &&\
		pip install -r requirements.txt --user

lint:
	python -m pylint --disable=R,C cli.py

format:
	python -m black *.py

test:
	python -m pytest --vv -cove=cli test_cli.py