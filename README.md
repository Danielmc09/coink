# coink

This application was created to register a user, validating input parameters and listing the information of registered users.

## Clone the repository

```bash
https://github.com/Danielmc09/coink.git
```
## Create virtual env and activate 

```bash
create:
  virtualenv name_env 
  
activate:
  On Unix or MacOS, using the bash shell: source venv/bin/activate
  On Windows using the Command Prompt: path\venv\Scripts\activate.bat
```
## install libraries

```bash
pip install -r requirements.txt
```
## run proyect

```bash
python manage.py runserver
```
## create migrations

```bash
- python manage.py makemigration
- python manage.py migrate
```
## Note 

- the database used in this project is sqlite3

- Ports to use that should not be busy or with local services turned off:
  - Django: 8000

|Path|Verb|Body params|
|----|----|----|
|Local|
|http://127.0.0.1:8000/registerUser/|POST|full_name - email - city|
|http://127.0.0.1:8000/listUser/|GET||


Autor: Angel Daniel Menideta Castillo © 2022
