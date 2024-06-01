

docker_run:
	docker-compose -f docker-compose.yml up -d --remove-orphans
	#poetry run python3 -m alembic upgrade head
	docker ps -a

docker_clean:
	docker rm -f `sudo docker ps -qa`
	docker rmi -f `sudo docker images -qa`
	docker volume prune -a
	docker network prune
	docker system prune --volumes
