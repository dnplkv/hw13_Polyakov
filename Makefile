include .env
export $(shell sed 's/=.*//' .env)

MANAGE = python main/manage.py
MAIN_APP = main
MAIN_DIR = main

run:
	$(MANAGE) runserver

make-migrate:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

freeze:
	pip freeze > requirements.txt

rabbit_run:
	systemctl enable rabbitmq-server
	systemctl start rabbitmq-server

rabbit_status:
	systemctl status rabbitmq-server

celery:
	cd $(MAIN_DIR) && celery -A $(MAIN_APP) worker --autoscale=4,2 -l info

beat:
	cd $(MAIN_DIR) && celery -A $(MAIN_APP) beat -l info

worker-info:
	cd $(MAIN_DIR) && celery -A $(MAIN_APP) events

shell:
	$(MANAGE) shell_plus --print-sql
