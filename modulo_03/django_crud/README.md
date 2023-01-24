# Django - CRUD

## First steps

### Starting the Django Project:

```
django-admin startproject {{project name}}
```

Updates in files:

*settings.py*
```
# update
TEMPLATES = [
  {
    DIRS = ['templates']
  }
]

# add
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```


### Starting the first App:

```
django-admin startapp {{app name}}
```

Updates in files:

*settings.py*
```
# update
INSTALLED_APPS = [
  ...,
  {{app name}}
]
```

Creating new files:

```
touch {{app}}/urls.py
touch {{app}}/forms.py
```

Creating new folders:

```
mkdir {{app}}/templates
mkdir {{app}}/static (this is where the css and js exteral data will be stored)
```

### Making Migrations

After creating a model inside the *models.py* file, you must register this model inside the *admin.py* file, as follows:
```
admin.site.register({{model}})
```

Then all you have to do is:

```
python manage.py makemigrations
python manage.py migrate
```


### Creating superuser

```
python manage.py createsuperuser
```

### Running tests

```
pip install coverage
coverage run manage.py test
coverage report
coverage html
python -m http.server
```