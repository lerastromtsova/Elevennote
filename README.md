# Elevennote

## Description

This is a TO-DO list project that allows a user to create notes, edit and delete them. It supports rich notes markup implemented with django-WYSIWYG. 

It is an educational project created during my second year of studies at ITMO University.

The project consisis of several apps:

### Accounts

An app for user management.


### Api

An app providing REST API.


### Notes

An app providing the functionality of a TO-DO list, including CRUD for notes.

## Technology stack

The backend is implemented with Python+Django with uWSGI and NGINX. The frontend part is implemented with Django templates and Bootstrap for nice CSS.

## Demo

Video demonstration is available here: https://bit.ly/3bebHwi

## Setup instructions

- You will need Postgres and Docker installed
- Create a file settings.ini in the root of the project. The template of the file is the following:
```
[settings]
SECRET_KEY={DJANGO_SECRET_KEY}
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
- Run `docker-compose up` from the root directory
- Go to http://127.0.0.1:8000/ and enjoy 🎉

## How to use / User story

- A user signs up in the system using an email/username and password
- On the home page, the user can create a new note
- After saving the note, the user sees a list of their notes
- Each note can be modified and/or deleted
- The user can log out and log in back again
