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

# About the settings splitted
Thanks to [`django-split-settings`](https://github.com/wemake-services/django-split-settings), I can split Django's original `settings.py` into multiple
business conf files.
```shell
# tree config/settings 
config/settings
├── components
│   └── common.py
├── environments
│   └── development.py
└── __init__.py

2 directories, 3 files
```

- If you need to split settings by components, add your component settings in the `components` directory.
- If you need to split settings by environments(this is quite common in multiple production env), add your component settings in the `environments` directory.
- `config/settings/__init__.py` holds the entrance for all settings, with the definition of `include` sequences.