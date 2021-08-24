#!/bin/sh

set -e

echo "Checking that the database is running..."
ping db -c 2

echo "Applying any pending migrations..."
python manage.py makemigrations

echo "Running migrations..."
python manage.py migrate

echo "Initializing Gunicorn..."
gunicorn -b 0.0.0.0:8000 -w 5 djangoapi.wsgi
