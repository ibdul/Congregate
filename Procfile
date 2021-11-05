web: npm start 
web: python manage.py collectstatic
web: python manage.py makemigrations
web: python manage.py migrate
web: gunicorn congregate.wsgi
