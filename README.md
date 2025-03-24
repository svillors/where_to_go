# Where to go
Online map based on Django

## Launch
To run the site, you will need Python 3.

Download the code from GitHub. Install the dependencies:
```
pip install -r requirements.txt
```
Create the SQLite database:
```
python3 manage.py migrate
```
Create `.env` file and set environment variables.
### variables
- DEBUG = debug mode. Set to True to see debug information in case of an error.
- DJANGO_SECRET_KEY - project secret key.
- ALLOWED_HOSTS - [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


Start the development server:
```
python3 manage.py runserver
```

## Demo
This repository is live at: [pythonanywhere](https://vilor.pythonanywhere.com/)