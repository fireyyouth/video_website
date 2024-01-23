# video website demo

## requirement
```
python3
django
djangorestframework
psycopg
```

## config postgres database
```
change DATABASES password in settings.py
```

## migrate schemas
```
python3 manage.py makemigrations
python3 manage.py migrate

```
## load test data
```
python3 manage.py shell < init_data.py
```

## run test server
```
python3 manage.py runserver 0.0.0.0:8000
```

## access from browser
```
visit "http://127.0.0.1:8000/static/index.html" in browser
```
