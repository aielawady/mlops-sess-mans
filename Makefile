install:
	pip install -r requirements.txt

lint:
	pylint hello.py

test:
	python -m pytest -vv

deploy:
	uvicorn app:app --host 0.0.0.0 --port 8000
