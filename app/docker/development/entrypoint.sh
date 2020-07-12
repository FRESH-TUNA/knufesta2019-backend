#!/bin/sh

EXPOSE_PORT=8000

echo -e "postgres running check "
until pg_isready -h database; do
  >&2 echo -e "."
  sleep 3
done
echo \ "postgres loaded! development server start!"

python3 /app/manage.py runserver 0.0.0.0:$EXPOSE_PORT
