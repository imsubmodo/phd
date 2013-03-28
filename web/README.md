
# Admininstration

## Create web site
django-admin.py startproject mysite

## Create superuser
python manage.py createsuperuser --username=imsubmodo --email=imsubmodo@gmail.com


# Manage

## Start Django Development server
python manage.py runserver

## Synchronize database
python manage.py syncdb

## Create application with name 'polls'
python manage.py startapp polls

## Print database creation for 'polls' appliaction
python manage.py sql polls

## Checks for any errors in the construction of your models.
python manage.py validate

## Outputs any custom SQL statements (such as table modifications or constraints) that are defined for the application.
python manage.py sqlcustom polls

## Outputs the necessary DROP TABLE statements for this app, according to which tables already exist in your database (if any).
python manage.py sqlclear polls

## Outputs the CREATE INDEX statements for this app.
python manage.py sqlindexes polls

## A combination of all the SQL from the sql, sqlcustom, and sqlindexes commands.
python manage.py sqlall polls 

## Synchronize database
python manage.py syncdb

## Invoke python shell
python manage.py sqlcustom polls
