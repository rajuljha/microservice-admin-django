#!/bin/bash
function wait_for_db()
{
  while ! ./manage.py sqlflush > /dev/null 2>&1 ;do
    echo "Waiting for the db to be ready."
    sleep 1
  done
}

wait_for_db
exec python manage.py runserver 0.0.0.0:8000