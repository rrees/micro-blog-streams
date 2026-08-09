
serve:
	pipenv run python runserver.py

deploy:
	flyctl deploy

update:
	pipenv update