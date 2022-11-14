# DJANGO STARTER PROJECT

- Run the following command to create a virtual environment for the project:

```
python3 -m venv env
```

- A folder name _env_ will be created. You should put the env folder on gitignore file.
- Activate the virtual environment:

```
source env/bin/activate
```

- To install the requirements:

```
pip install -r requirements.txt
```

- A project is created using django-admin which created the config folder.
- The config folder has a folder named _settings_ which contains different settings file for different environment.
- The settings file is named _base.py_ which is the base settings file.
- Now you can edit the .env file to set the environment variables.
- The .env file is used to set the environment variables.
- Make a .env file as .env_example file.
- The secret key is used of env file can be generated using python manage.py shell command.

```
python manage.py shell
```

- Use these commands to generate a secret key through the shell:

```
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

- Change your DJANGO_SETTINGS_MODULE to **settings.local** or **settings.production** depending on your needs use the command

```bash
export DJANGO_SETTINGS_MODULE=config.settings.local
```

```bash
export DJANGO_SETTINGS_MODULE=config.settings.production
```

- Create new django app using the following command:

```
python manage.py startapp <app_name>
```

- For app's folder and file structure follow the demoapp.
- The app's folder structure is as follows:

```
.
├── apps
│   ├── demoapp
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── v1
│   │   │   ├── __init__.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   └── v2
│   │       ├── __init__.py
│   │       ├── urls.py
│   │       └── views.py
│   ├── __init__.py
│   └── tasks            # This app will contain all the commands and tasks
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── management
│       │   ├── commands
│       │   │   ├── createsu.py
│       │   │   └── __init__.py
│       │   └── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       └── urls.py
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
└── requirements.txt
```

- Run the project using the following command:

```
python manage.py runserver
```

- To test the demo app use the link below:

```
For version 1 of the API
http://127.0.0.1:8000/api/v1/demo/
For version 2 of the API
http://127.0.0.1:8000/api/v2/demo/
```

## Notes

The demo app contains a custom version of django's default **manage.py createsuperuser** command.
To create super user using this custom command use the following command:

```
  manage.py createsu \
          --username foo     \
          --password foo     \
          --email foo@foo.foo
```
