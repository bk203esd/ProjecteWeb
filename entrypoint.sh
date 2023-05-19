#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "Creating superuser"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 'root@root.com', 'root')" | python manage.py shell

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

# Execute curl command
echo "Executing curl command"
#sudo apt install curl -y
curl http://localhost:8000/api/db/