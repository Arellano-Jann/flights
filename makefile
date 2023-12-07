all:
	python3 algo.py

dep:
	pip3 install numpy pandas matplotlib networkx seaborn

svelte:
	npm create svelte@latest frontend
	cd frontend
	npm install

django:
	pip3 install django django-rest-framework django-cors-headers

backend:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver

fresh:
	sudo apt-get update
	sudo apt install python3-pip3
	sudo apt install make
	make dep
	make all
