# Django-FSD-lab

## INDEX
1. [Cloning the Repository](#cloning-the-repository)
2. [Installation](#installation)
3. [Project Creation](#project-creation)
4. [Running the Program](#running-the-program)
5. [App Creation](#app-creation)
    - [Current Date and Time](#current-date-and-time-ap1)
    - [Time Delta](#time-delta-ap1)
    - [Templates](#templates-ap2)
    - [Template Inheritance](#template-inheritance-ap3)
    - [Models](#models-ap4)
    - [Admin Interface](#admin-interface-ap4)
    - [Model Form](#model-form-ap4)
    - [Generic Views](#generic-views-ap4)
    - [CSV and PDF gen](#csv-and-pdf-gen-ap4)
    - [Registration using AJAX](#registration-using-ajax-ap4)
    - [Search using AJAX](#search-using-ajax-ap4)
6. [Setting Up the Local System Environment](#setting-up-the-local-system-environment)

## Cloning the Repository

To clone the repository, use:

```bash
git clone https://github.com/Akp-arvind/Django-FSD-lab
```

## Installation

 - Libraries: You can install the required libraries using pip. Open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```

 - Download and install the XAMPP server
```bash
https://www.apachefriends.org/download.html
```

**OR**

 - Download and install WAMP server
```bash
https://sourceforge.net/projects/wampserver/files/latest/download
```
 - For WAMP, many files will be missing and the system asks to install them. Hence download the files from this website:
```bash
https://wampserver.aviatechno.net/
```
(Last link ; chose second file after getting redirected ; Windows_64_bit) <br>

## Project creation

Open the terminal and enter the following command:
```bash
django-admin startproject <project_name>
```
( e.g. - "lab" )

Observe that some files are generated.

## Running the Program

Once you have installed the necessary libraries, and satisfied the program specific requirements, you can run the program by following these steps:

1. Navigate to the project directory using the terminal or command prompt.
- Ensure that XAMPP/WAMP server is running (if required).
2. Run the following command to start the Django server:

```bash
python manage.py runserver
```

3. Open your web browser and enter the following URL:

```bash
http://localhost:8000
```
OR
```bash
http://127.0.0.1:8000
```

You should now be able to access the program. <br>
You would have to enter the path manually this way.

## App creation

To create an app, enter the following command in the terminal:
```bash
python manage.py startapp <app_name>
```
( e.g. -  "ap2" )

In _settings.py_ file, under TEMPLATES, set:
```bash
'DIRS':[os.path.join(BASE_DIR,'ap2/templates')],
```
This will ensure that the templates for the "ap2" app are accessible.


1. ### Current date and time (ap1)
```bash
http://localhost:8000/cdt/
```
2. ### Time delta (ap1)
```bash
http://localhost:8000/fhb/
```
```bash
http://localhost:8000/fha/
```
3. ### Templates (ap2)
```bash
http://localhost:8000/showlist/
```
4. ### Template Inheritance (ap3)
```bash
http://localhost:8000/home/
```
 - Navigation can be done via clicking the links 
 - Observe the changes in URL after clicking
5. ### Models (ap4)

 - After successful installation of the server from [Installation](#installation) segment, start it and go to:
```bash
http://localhost/phpmyadmin
```
 - Create a new database - “studentreg” (db name)

 - In _settings.py_ file:
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ap4', # added
]
```
```bash 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        # changed from sqlite3 default
        'NAME': 'studentreg', 
        # changed for ap4
        'USER': 'root', 
        'PASSWORD': '', 
        'HOST':'localhost', 
        'PORT':'3306',
    }
}
```
```bash
STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, 'ap4/static')] 
# added
```
 - Make [migrations](#migrations) to the db:
```bash
python manage.py makemigrations ap4
```
```bash
python manage.py migrate
```
 - Add entities in the database tables (ap4_student and ap4_course)
 - ### NOTE: migrations should be done every time _models.py_ changes or any database table changes.

Finally, for viewing the output, run the code and open your web browser to enter the followinbg URL:
```bash
http://localhost:8000/reg/
```
 - Remember to stop the server once you're done.
```bash
http://localhost:8000/course_search/
```
6. ### Admin Interface (ap4)

 - Changes made to the code have been indicated in the comments.

 - Set the username and password by entering the following command in the terminal:
```bash
python manage.py createsuperuser
```
 - Make changes to the db using the admin UI.

To login, enter the following URL in your web browser:
```bash
http://localhost:8000/admin/
```
7. ### Model Form (ap4)
 - Perform migrations if required, run the app and go to:
```bash
http://localhost:8000/add_project/
```
 - Add the indicated fields.
 - The changes can be viewed here (ap4_project):
```bash
http://localhost/phpmyadmin
```
8. ### Generic Views (ap4)
 - Use the following paths for getting generic and detailed views (pre-registered students):
```bash
http://localhost:8000/student_list/
```
```bash
http://localhost:8000/student_detail/
```
 - /<int: pk>/ (primary key, e.g. - "/2/") can be apppended here which will display the details of the corresponding student. 

9. ### CSV and PDF gen (ap4)
 - Ensure that the data has been inserted beforehand.
 - 9 A
```bash
http://localhost:8000/construct_csv_from_model/
```
 - 9 B
```bash
http://localhost:8000/construct_pdf_from_model/
```
 - Observe that the files get downloaded as soon as the path is entered.

10. ### Registration using AJAX (ap4)
 - Ensure that "jquery.min.js" file is present in the static folder.
```bash
http://localhost:8000/regaj/
```
 - Observe that the output is displayed on the same web page (reloading is not required, thanks to Ajax).

11. ### Search using AJAX (ap4)
```bash
http://localhost:8000/course_search_ajax/
```
 - Again, the partial output is loaded on the same page.

<br>
<hr>
<hr>

## Setting Up the Local System Environment

1. Create a new folder for your project.
2. Open the command prompt and navigate to the newly created folder.
3. Enter the following command to create a virtual environment named "env":

```bash
python -m venv env
```

This will create a new virtual environment in the "env" folder.

4. Activate the virtual environment by running the following command:

```bash
env\Scripts\activate
```

5. You can now install the necessary libraries and run the program as mentioned in the previous instructions.

If you're using VS Code, go to View - Command Palette - Python: Select Interpreter - 3.11.1 ( 'env':venv )

Remember to deactivate the virtual environment when you're done by running the following command:

```bash
deactivate
```

This will ensure that your system environment is properly set up for the project.
