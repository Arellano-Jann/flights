all:
	python3 algo.py

dependencies:
	pip3 install numpy pandas matplotlib networkx

fresh:
	sudo apt-get update
	sudo apt install python3-pip3
	sudo apt install make
	make dependencies
	make all