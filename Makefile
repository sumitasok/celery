bash:
	docker run -it --rm -v `pwd`:/app --name celery_bash celery_celery /bin/bash

log:
	tail -f celeryapp.log

down:
	docker-compose -f "docker-compose.yml" down

up:
	docker-compose -f "docker-compose.yml" up

flower:
	docker run -it --rm --name celery_flower -p 7072:7072 celery_celery celery flower --broker=$(broker) --port=7072