# GoTicket!

> If you just want to run the project, then run the following
and thats all. Note the `python manage.py runserver` assumes that your Python3 is set in your system PATH as the default path to run when python is called. Otheriwse use `python3 manage.py runserver`

```
~/GoTicket$ git clone https://github.com/pmburu/GoTicket.git
~/GoTicket$ cd GoTicket
~/GoTicket$ virtualenv venv
~/GoTicket$ source venv/bin/activate
(venv) ~/GoTicket$ pip install -r requirements.txt
(venv) ~/GoTicket$ python manage.py runserver
```

> Part of this README file is adapted from (https://github.com/DjangoGirls/tutorial/edit/master/en/django_start_project).

We're going to create a Ticketing project!

The first step is to start a new Django project. Basically, this means that we'll run some scripts provided by Django that will create the skeleton of a Django project for us. This is just a bunch of directories and files that we will use later.

The names of some files and directories are very important for Django. You should not rename the files that we are about to create. Moving them to a different place is also not a good idea. Django needs to maintain a certain structure to be able to find important things.

> Remember to run everything in the virtualenv. If you don't see a prefix `(venv)` in your console, you need to activate your virtualenv. We explained how to do that in the __Django installation__ chapter in the __Working with virtualenv__ part. Typing `venv\Scripts\activate` on Windows or
`source venv/bin/activate` on Mac OS X or Linux will do this for you.

<!--sec data-title="Create project: OS X or Linux" data-id="django_start_project_OSX_Linux" data-collapse=true ces-->

In your Mac OS X or Linux console, you should run the following command. **Don't forget to add the period (or dot) `.` at the end!**

```
(venv) ~/GoTicket$ django-admin startproject goticket .
```

> The period `.` is crucial because it tells the script to install Django in your current directory (for which the period `.` is a short-hand reference).

> **Note** When typing the command above, remember that you only type the part which starts by `django-admin`.
The `(venv) ~/GoTicket$` part shown here is just example of the prompt that will be inviting your input on your command line.

<!--endsec-->

<!--sec data-title="Create project: Windows" data-id="django_start_project_windows" data-collapse=true ces-->

On Windows you should run the following command. **(Don't forget to add the period (or dot) `.` at the end)**:

```
(venv) C:\Users\Name\GoTicket> django-admin.exe startproject goticket .
```
> The period `.` is crucial because it tells the script to install Django in your current directory (for which the period `.` is a short-hand reference).

> **Note** When typing the command above, remember that you only type the part which starts by `django-admin.exe`.
The `(venv) C:\Users\Name\GoTicket>` part shown here is just example of the prompt that will be inviting your input on your command line.

<!--endsec-->

`django-admin.py` is a script that will create the directories and files for you. You should now have a directory structure which looks like this:

```
GoTicket
├── manage.py
├── goticket
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv
│   └── ...
└── requirements.txt
```
> **Note**: in your directory structure, you will also see your `venv` directory that we created before.

`manage.py` is a script that helps with management of the site. With it we will be able (amongst other things) to start a web server on our computer without installing anything else.

The `settings.py` file contains the configuration of your website.

Remember when we talked about a mail carrier checking where to deliver a letter? `urls.py` file contains a list of patterns used by `urlresolver`.

Let's ignore the other files for now as we won't change them. The only thing to remember is not to delete them by accident!


## Changing settings

Let's make some changes in `goticket/settings.py`. Open the file using the code editor you installed earlier.

**Note**: Keep in mind that `settings.py` is a regular file, like any other. You can open it from inside the code editor, using the "file -> open" menu actions. This should get you the usual window in which you can navigate to your `settings.py` file and select it. Alternatively, you can open the file by navigating to the goticket folder on your desktop and right-clicking on it. Then, select your code editor from the list. Selecting the editor is important as you might have other programs installed that can open the file but will not let you edit it.

It would be nice to have the correct time on our website. Go to [Wikipedia's list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) and copy your relevant time zone (TZ) (e.g. `Europe/Berlin`).

In `settings.py`, find the line that contains `TIME_ZONE` and modify it to choose your own timezone.  For example:

```python
TIME_ZONE = 'Europe/Berlin'
```

A language code consist of the language, e.g. `en` for English or `de` for German, and the country code, e.g. `de` for Germany or `ch` for Switzerland. If English is not your native language, you can add this to change the default buttons and notifications from Django to be in your language. So you would have "Cancel" button translated into the language you defined here. [Django comes with a lot of prepared translations](https://docs.djangoproject.com/en/2.2/ref/settings/#language-code).

If you want a different language, change the language code by changing the following line:

```python
LANGUAGE_CODE = 'en-UK'
```


We'll also need to add a path for static files. (We'll find out all about static files and CSS later in the tutorial.) Go down to the *end* of the file, and just underneath the `STATIC_URL` entry, add a new one called `STATIC_ROOT`:

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
```

When `DEBUG` is `True` and `ALLOWED_HOSTS` is empty, the host is validated against `['localhost', '127.0.0.1', '[::1]']`. This won't
match our hostname on PythonAnywhere once we deploy our application so we will change the following setting:

```python
ALLOWED_HOSTS = ['127.0.0.1', 'anyotherexternalurl']
```

> **Note**: If you're using a Chromebook, add this line at the bottom of your settings.py file:
> `MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'`

> Also add `.amazonaws.com` to the `ALLOWED_HOSTS` if you are using cloud9

> If you are hosting your project on `Glitch.com`, let us protect the Django secret key that needs to
> remain confidential (otherwise, anyone remixing your project could see it):
>
>   * First, we are going to create a random secret key.
>     Open the Glitch terminal again, and type the following command:
>
>    
>     ```bash
>     python -c 'from django.core.management.utils import get_random_secret_key; \
>           print(get_random_secret_key())'
>     ```
>     This should display a long random string, perfect to use as a secret key for your brand new Django web site.
>     We will now paste this key into a `.env` file that Glitch will only show you if you are the owner of the web site.    
>   
>   * Create a file `.env` at the root of your project and add the following property in it:
>
>    
>     ```bash
>     # Here, inside the single quotes, you can cut and paste the random key generated above
>     SECRET='3!0k#7ds5mp^-x$lqs2%le6v97h#@xopab&oj5y7d=hxe511jl'
>     ```
>   * Then update the Django settings file to inject this secret value and set the Django web site name:
>
>  
>     ```python
>     SECRET_KEY = os.getenv('SECRET')
>     ```
>   * And a little further down in the same file, we inject the name of your new Glitch website:
>
>    
>     ```python
>     ALLOWED_HOSTS = [os.getenv('PROJECT_DOMAIN') + ".glitch.me"]
>     ```
>     The `PROJECT_DOMAIN` value is automatically generated by Glitch.
>     It will correspond to the name of your project.

## Set up a database

There's a lot of different database software that can store data for your site. We'll use the default one, `sqlite3`.

This is already set up in this part of your `goticket/settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
NOTE: It is not recommended to run migrations before 'fixing' creating the type of user attributes you would like to have in your project.
Django migrations are sensitive files that can be broken easily with data integrity issues. Therefore, we create the users and user types first.

To create a database for our project, let's run the following in the console: `python manage.py migrate` (we need to be in the `goticket` directory that contains the `manage.py` file). If that goes well, you should see something like this:

```
(venv) ~/GoTicket$ python manage.py migrate
Operations to perform:
  Apply all migrations: auth, admin, contenttypes, sessions
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying sessions.0001_initial... OK
```

And we're done! Time to start the web server and see if our website is working!

## Starting the web server

You need to be in the directory that contains the `manage.py` file (the `GoTicket` directory). In the console, we can start the web server by running `python manage.py runserver`:

```
(venv) ~/GoTicket$ python manage.py runserver
```

If you are on a Chromebook, use this command instead:

```
(venv) ~/GoTicket$ python manage.py runserver 0.0.0.0:8080
```
or this one if you are using Glitch:

```
$ refresh

```

If you are on Windows and this fails with `UnicodeDecodeError`, use this command instead:

```
(venv) ~/GoTicket$ python manage.py runserver 0:8000
```


Now you need to check that your website is running. Open your browser (Firefox, Chrome, Safari, Internet Explorer or whatever you use) and enter this address:

```
http://127.0.0.1:8000/
```

If you're using a Chromebook and Cloud9, instead click the URL in the pop-up window that should have appeared in the upper right corner of the command window where the web server is running. The URL will look something like:

```
https://<a bunch of letters and numbers>.vfs.cloud9.us-west-2.amazonaws.com
```
or on Glitch:
```
https://name-of-your-glitch-project.glitch.me
```

Congratulations! You've just created your first website and run it using a web server! Isn't that awesome?

![Install worked!](https://github.com/DjangoGirls/tutorial/blob/master/en/django_start_project/images/install_worked.png)

Note that a command window can only run one thing at a time, and the command window you opened earlier is running the web server. As long as the web server is running and waiting for additional incoming requests, the terminal will accept new text but will not execute new commands.

> We reviewed how web servers work in the <b>How the Internet works</b> chapter.

To type additional commands while the web server is running, open a new terminal window and activate your virtualenv -- to review instructions on how to open a second terminal window, see [Introduction to the command line](../intro_to_command_line/README.md). To stop the web server, switch back to the window in which it's running and press CTRL+C - Control and C keys together (on Windows, you might have to press Ctrl+Break).

Ready for the next step? It's time to create some content!

## Creating a new module

You need to be in the directory that contains the `manage.py` file (the `GoTicket` directory). In the console, we can start the web server by running `python manage.py startapp app_name`:


Then you will see a file system like below

```
GoTicket
├── manage.py
├── goticket
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_name
|   ├── migrations
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── venv
│   └── ...
└── requirements.txt
```
