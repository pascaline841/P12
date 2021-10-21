<h1 align="center">REST API Project - EPIC EVENTS - OpenClassRooms Project 12</h1>
<br>
<br>
Ce script Python est le 12e projet réalisé dans le cadre d'une formation chez OpenClassrooms.
<br>

## OVERVIEW
Beta version of a RESTful API made with Django REST Framework. 
Epic Events is an event management and consulting company that meets the needs of start-ups wanting to organize “epic parties”.<br>
It should allow different CRM operations to different types of user groups depending on their permissions.
<br> 
The access is granted to authenticated users via JSON Web Tokens (JWTs).

## REQUISITORIES
Python 3 <br>
Django 3 <br>
Django REST Framework 3 <br>
<br>

## INSTALLATION
Start by closing the repository :
```
git clone https://github.com/pascaline841/p12
```
Start access the project folder

## for Window
Create a virtual environment
```
python -m venv env
```
Enable the virtual environment
```
cd env/scripts
source activate
```

## for Linux or macOS
Create a virtual environment 
```
python3 -m venv env
```
Activate the virtual environment with 
```
source env/bin/activate 
```
## . . . 
Install the python dependencies to the virtual environment
```
pip install -r requirements.txt
```
Create and open a file named .env then paste :
```
SECRET_KEY=''
```
Then complete SECRET_KEY with the key you receive in private.

## DATABASE by PostgreSQL
Create the database structure by using PostgreSQL
```
CREATE USER admin WITH ENCRYPTED PASSWORD 'OCPython2021';
```
```
ALTER ROLE admin SET client_encoding TO 'utf8';
```
```
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
```
```
CREATE DATABASE epicevents;
```
```
GRANT ALL PRIVILEGES ON DATABASE epicevents TO admin;
```
Now you can apply the migrations 
```
python manage.py migrate
```
<br>
Create a superuser account :<br>
(to used a preset database is below)<br>
You will be asked to select a username, provide an email address, and choose and confirm a password for the account.
```
python manage.py createsuperuser
```

## EXECUTION
Run the program
```
python manage.py runserver
```
Launch 
```
http://127.0.0.1:8000
```
To access to the admin account 
```
http://127.0.0.1:8000/admin
```
To log in and obtain JSON Web Token 
```
http://127.0.0.1:8000/login
```
## Test the API with POSTMAN
A Public Postman collection is available to test the API endpoints.
```
https://documenter.getpostman.com/view/16100693/UV5Ukeaa
```
## USER TESTS with a PRESET DATABASE
If you would like to test the API, there is a preset database with 1 admin and 4 users.
```
python manage.py migrate
```
```
python manage.py loaddata fixture/whole.json
```
Then, run the program. <br>
LOGIN : admin / sale / sale02 / support / support02<br>
PASSWORD : OCPython2021<br>