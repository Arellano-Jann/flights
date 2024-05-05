algo:
	python3 algo.py

pg_dump-%:
	docker exec -it db bash -c "pg_dump -U admin -d flights > /$*.sql"
	docker cp db:/$*.sql $*.sql

startdocker:
	sudo dockerd

rmdocker:
	rm -rf  ~/.docker

rmdockerconfig:
	rm ~/.docker/config.json

docker_image:
	docker build -t flights/backend:1.0 .

docker_run-%:
	docker run -p 8000:8000 $*

docker_compose_up:
	docker-compose up -d --build

docker_compose_down:
	docker-compose down

docker_compose_down_all:
	docker-compose down --rmi all --volumes

docker_compose_stop:
	docker-compose stop