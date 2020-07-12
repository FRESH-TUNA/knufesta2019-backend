#!/bin/sh

echo -e "postgres running check "
until pg_isready -h database; do
  >&2 echo -e "."
  sleep 3
done
echo \ "postgres loaded! processing migration..."

python3 /app/manage.py makemigrations
python3 /app/manage.py migrate
echo "migration success!"
