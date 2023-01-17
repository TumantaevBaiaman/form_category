## Setup

Create and activate a virtual environment (Python3) using your preferred method. This functionality is [built into](https://docs.python.org/3/tutorial/venv.html) Python, if you do not have a preference.

From the command line, type:

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Setup mongodb in settings.py
```
DATABASES = {
   'default': {
       'ENGINE': 'djongo',
       'NAME': 'name_db',
   }
}
```

Create superuser

```
python manage.py createsuperuser
```

Run project
```
python manage.py runserver
```

Open your browser to http://localhost:8000 and you should see the browsable version of the API.

# api
```
- /admin/               - admin
- /form/create/         - url create from
- /form/get_form/            - url get from
```

# Validate form and fields
```
form:     name      - unique=True

fields:   email     - email@gmail.com
          phone     - +7 xxx xxx xx xx
          text      - none
          date      - YYYY-MM-DD
```

# Example of create form
***
```
url: /form/create/ 
{
    "name": "form_name",
    "email": "email@gmail.com",
    "phone": "+7 777 777 77 77",
    "text": "text form",
    "date": "2023-06-16"
}
```

# Example of get form
```
url: /form/get_form/ 
{
    "email": "email@gmail.com",
    "phone": "+7 777 777 77 77"
}
```
