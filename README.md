# pipauls

## Purpose

Pipauls is an application t share and exchange Do It Yourself product

Every member can add its DIY product and propose exchange with other member in his region

## Technical stack

Build in Django

### Prerequisit

Install:
* Docker
* Docker-compose

Used technologies:
* Python and Django
* Docker and Docker-compose
* Postgresql (as DB)
* Bootstrap (as rendering framework)

### Run it locally

Run the DB using docker-compose

````shell script
docker-compose up -d
````
NB: perhaps the first execution will failed because of the delay to create the database instance, please retry

Apply the migration

````shell script
docker-compose exec pipauls python manage.py migrate
````

Run the application using Django command

````shell script
docker-compose exec pipauls python manage.py runserver
````

Access to the application locally : http://localhost:8000/exchange

Stop the application

````shell script
docker-compose down
````

Force to relaunch the application

````shell script
docker-compose restart
````

Rebuild the application after adding a package in the requirements.txt

````shell script
docker-compose rebuild
````

### Admin

To manage admin access, create a superuser:

````shell script
docker-compose exec pipauls python manage.py createsuperuser
````

Add access to admin locally : http://localhost:8000/admin

