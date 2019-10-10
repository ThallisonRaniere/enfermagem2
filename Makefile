user:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0:8000

shell:
	python manage.py shell_plus

static:
	python manage.py collectstatic --noinput
