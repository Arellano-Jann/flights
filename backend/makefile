all:
	make migrate
	make run 

django:
	pip3 install django django-rest-framework django-cors-headers
	# django-admin startproject backend

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

run:
	python3 manage.py runserver
