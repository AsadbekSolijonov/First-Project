mig:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

user:
	python manage.py createsuperuser --username admin --email iamsolijonov@gmail.com

seed:
	python manage.py seed news --number=15