# django-react-boilerplate
This a simple django-react fullstack boilerplate setup.

# Start with PDM(Python Libraries)
```shell
# Create project for the first time
mkdir project_dir
cd project_dir

pdm init
pdm add django djangorestframework django-cors-headers

# Install 3rd python libraries
pdm install
```

# Continue with Yarn(React Frontend)
```shell
cd project_dir
# Use `npm install yarn -g`, if yarn is not installed
yarn create react-app frontend
cd frontend
yarn add axios
```

# Continue with Django RestAPI setup
```shell
cd project_dir

source .venv/bin/activate
django-admin startproject config . # It's my habbit to use `config` directory for django settings
./manage.py startapp api           # api will be the only app in this django project 
```

# Now the Django settings
```shell
INSTALLED_APPS = [
    # ...
    # 👇 Add here your installed app's
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    # ...
    # 👇 Add this line here
    'corsheaders.middleware.CorsMiddleware',
    # Add above line just before this line 👇
    'django.middleware.common.CommonMiddleware',
]

# 👇 Add this line here
CORS_ORIGIN_ALLOW_ALL = True
```

# Create a simple GET view(Backend)
```shell
# Add these in api/views.py
# This code defines a new API endpoint that returns a JSON response with the message “Hello, world!”.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})
```

# Add urlpattern(Backend)
```shell
# Add these in config/urls.py
from django.contrib import admin
from django.urls import path, include # 👈 Add include here

urlpatterns = [
    path('admin/', admin.site.urls),
    # 👇 add your myapi app urls path here
    path('api/', include('api.urls'))
]

# Create app/urls.py and add these lines
from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
]
```

# Create a new component in frontend/src (Frontend)
# Render the new component in App.js (Frontend)

# Development
See [HOWTO-Dev.md](./HOWTO-Dev.md)

# Dockerize
See [HOWTO-Dockerize.md](./HOWTO-Dockerize.md)