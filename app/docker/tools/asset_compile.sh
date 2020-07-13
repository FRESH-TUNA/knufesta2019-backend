#!/bin/sh
python3 /app/manage.py compilescss
python3 /app/manage.py collectstatic --no-input --ignore=*.sass
python3 /app/manage.py compilescss --delete-files
