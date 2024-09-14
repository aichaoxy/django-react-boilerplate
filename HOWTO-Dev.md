# Debug the project
```shell
# You need two terminals
# Terminal 1  - start the Django development server.
./manage.py makemigrations
./manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
./manage.py runserver

# Terminal 2 - start the React development server.
cd ./frontend && yarn start
```