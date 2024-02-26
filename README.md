This workspace is founded on a template provided by Code Institute

Setup
===
Django
---
- In terminal:
`pip3 install 'django<4'`

Django project:
---
- Not to be confused with Django app, the project holds files such as settings.py and manage.py
- In terminal:
`django-admin startproject django_todo .`
- The dot install the project at the current (root) directory

Django app:
---
- In terminal:
´python3 manage.py startapp todo´
- Apps can function without being added to installed apps, but with limited functionality:
Unable to render html templates


Etc
===

Migrations:
---
`python3 manage.py makemigrations --dry-run`
`python3 manage.py showmigrations`
`python3 manage.py makemigrations`
`python3 manage.py migrate --plan`
`python3 manage.py migrate`

Show item name
---
The following code:
`
    def __str__(self):
        return self.name
`
is used to return the name of an object, rather than "Item object (indx)"

Flake8
---
- Python standard checking using Flake8