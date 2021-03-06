# Local DB, Users
* super admin user: rob, P@ssword1
* admin user: temp, P@ssword1

# Some Important Environment Info for Python & Django Projects
`pyenv shell` to get a shell loaded with the project's dependencies (including django)

# Some Important Commands Used in this Tutorial
`python manage.py runserver`

## General Startup and Maintenance Commands

### To Create a project
  1. create an env in which django can run (pyenv + pipenv, not used in tut)
  2. mkdir <myproject> && cd <myproject>
  3. `django-admin startproject <myproject>`

### To create an APP inside the django PROJECT
  1. `python manage.py startapp <my_app_name>`
  2. add application to list of installed apps in settings.py
  3. import <my_app_name> URLs into the project URLs (e.g. `path('catalog/', include('catalog.urls'))`)

### Adding Models
  1. Simply code your models in an app's `models.py` file
  2. run migrations (see below)

### To run migrations
  1. `python manage.py makemigrations`
  2. `python manage.py migrate`

### To create a superuser in the admin panel
  `python manage.py createsuperuser`




## Library of Useful Commands by Topic

### Database / ORM Stuff
  * `migrate`, which is responsible for applying and unapplying migrations.
  * `makemigrations`, which is responsible for creating new migrations based on the changes you have made to your models.
  * `sqlmigrate`, which displays the SQL statements for a migration.
  * `showmigrations`, which lists a project’s migrations and their status.


## Auth
* Use the built-in library to create users
* Endpoints are created for you have to create the templates yourself, in root/templates
* There are a couple helpful lines at the end of `settings.py` related to Auth
* The default password system uses email links to reset passwords; you have to set up emails manually
* Checking if users are logged in, with redirect behavior:
    * Function-based views: use the `@login_required` decorator (equivalent to request.user.is_authenticated)
    * Class-based views: derive from LoginRequiredMixin by adding it to the superclass view
        * `class MyView(LoginRequiredMixin, View)`
        * declare this before you declare the main view class
