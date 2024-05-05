#!/bin/sh

# This simply checks that Postgres is accessible before allowing
# everything else to proceed.

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# make purge

exec "$@"