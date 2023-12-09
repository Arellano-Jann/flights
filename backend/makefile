all:
	make migrate
	make run 

django:
	pip3 install django django-rest-framework django-cors-headers
	# django-admin startproject backend

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

migrate-first-run:
	make sync
	make migrate

sync:
	python3 manage.py migrate --run-syncdb

fake:
	python3 manage.py migrate --fake flights

run:
	python3 manage.py runserver
