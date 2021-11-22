FLASK_APP=app.py

.PHONY: default
default:
	flask run

test:
	python -m unittest
