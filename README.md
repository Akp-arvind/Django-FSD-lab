# Django-FSD-lab

To clone the repository, use:

```bash
git clone https://github.com/Akp-arvind/Django-FSD-lab
```

## Installation

You can install the following libraries using pip. Open your terminal or command prompt and run the following command:

```bash
pip install -r requirements.txt
```
## Project creation

Open terminal and enter the following command:
```bash
django-admin startproject <project_name>
```
( e.g. - "lab" )

Observe that some files are generated.

## Running the Program

Once you have installed the necessary libraries, and satisfied the program specific requirements, you can run the program by following these steps:

1. Navigate to the project directory using the terminal or command prompt.
2. Run the following command to start the Django server:

```bash
python manage.py runserver
```

3. Open your web browser and enter the following URL:

```bash
http://localhost:8000
```
You should now be able to access the program. <br>
You would have to enter the path manually this way.

## App creation

To create an app, enter the following command in the terminal:
```bash
python manage.py startapp <app_name>
```
( e.g. -  "ap2" )

In settings.py file, under TEMPLATES, set:
```bash
'DIRS':[os.path.join(BASE_DIR,'ap2/templates')],
```
This will ensure that the templates for the "ap2" app are accessible.


1. Current date and time (ap1)
```bash
http://localhost:8000/cdt/
```
2. Time delta (ap1)
```bash
http://localhost:8000/fha/
```
3. Templates (ap2)
```bash
http://localhost:8000/showlist/
```
4. Template Inheritance (ap3)
```bash
http://localhost:8000/home/
```
5. Models (ap4)
Download and install the XAMPP server
```bash
https://www.apachefriends.org/download.html
```
OR <br>
WAMP server
```bash
https://sourceforge.net/projects/wampserver/files/latest/download
```
For WAMP, many files will be missing and system 
asks to install it. Hence download the files from this website:
```bash
https://wampserver.aviatechno.net/
```
(Last link ; chose second file after getting redirected ; Windows_64_bit) <br>

After successful installation of the server, start it and go to:
```bash
http://localhost/phpmyadmin
```
Create a new database - “studentreg” (db name)




Finally, for viewing the output, open your web browser and enter the followinbg URL:
```bash
http://localhost:8000/reg/
```




<br>
<br>
<hr>


## In case you want to set up the local system environment from scratch, follow these steps:

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

If you're using VS Code, go to View -> Command Palette -> Python: Select Interpreter -> 3.11.1 ( 'env':venv )
Remember to deactivate the virtual environment when you're done by running the following command:

```bash
deactivate
```

This will ensure that your system environment is properly set up for the project.
