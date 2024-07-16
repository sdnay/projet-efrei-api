#!/bin/bash

# Attente de la disponibilité de MariaDB
if [ "$DATABASE" = "mariadb" ]; then
    echo "Waiting for MariaDB..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 1
    done
    echo "MariaDB is up - executing command"
fi

# Appliquer les migrations
echo "Applying database migrations..."
python manage.py migrate

# Créer un superutilisateur si nécessaire
echo "Creating superuser..."
python manage.py add_initial_data

# Démarrer le serveur Django
exec "$@"
