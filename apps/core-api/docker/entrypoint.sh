#!/bin/sh

set -e

echo "Checking Django configuration..."
python manage.py check

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000
