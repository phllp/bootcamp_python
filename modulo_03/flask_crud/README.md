# Flask 

## Project setup

```
python3 -m venv env
source ./env/bin/activate

pip install flask
pip install Flask-WTF
pip install Flask-Migrate
pip install flask-sqlalchemy==2.5.1

set FLASK_APP = app.py
flask run
```

## Migrations

```
flask db init
flask db migrate
flask db upgrade
```

## Testing

```
python3 -m unittest -v tests/test.py
```

## Important

### SQLAlchemy version

While testing requests, a problem envolving the database interation ocurred. 
The solution: downgrading the flask-sqlalchemy version from 3.0.2 to 2.5.1
