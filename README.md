# pipauls

## Purpose

Pipauls is an application t share and exchange Do It Yourself product

Every member can add its DIY product and propose exchange with other member in his region

## Technical stack

Build in Django

### Prerequisit

Install:
* Python3 (I recommend pyenv)
* Django
* Docker
* Docker-compose

### Run it locally

Run the DB using docker-compose

````shell script
docker-compose up -d
````

Apply the migration

````shell script
python manage.py migrate exchange
````

Run the application using Django command

````shell script
python manage.py runserver
````

Access to the application : http://localhost:8000/exchange

### Admin

To manage admin access, create a superuser:

````shell script
python manage.py createsuperuser
````

Add access to admin : http://localhost:8000/admin

