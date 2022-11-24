cd /code/
poetry install
poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate
poetry run python -m gunicorn --bind 0.0.0.0:8000 core.wsgi --workers=4