[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-1.11-brightgreen.svg)](https://djangoproject.com)



This project is school management system design for Godawari Residential School.

## Running the Project Locally (Development):

* First, clone the repository to your local machine:

```bash
git clone git@github.com:raeesaroj/schoolMIS.git
```
* Enter inside the project directory:

```bash
cd schoolsmis/
```
* Install the requirements by selecting where you want to run (base, developement, production) using pip:

```bash
pip install -r requirements.txt
```

*PS: If you have issues installing either `gunicorn` or `psycopg2`, you can remove them from the requirements.txt file and run the command again.*

* Create the database:

```bash
python manage.py migrate
```

* Enter inside the grs-react app:

```bash
cd schoolmis/grs-react/
```
* Run the following command to install the node modules:

```bash
npm install
```
* Finally run both the django development server as well as the webpack server(for react) using folllowing commands:

```bash
npm run start
```

```
python manage.py runserver
```


---


## For Production:

* First, clone the repository to your local machine:


```bash
git clone git@github.com:raeesaroj/schoolMIS.git
```

* Enter inside the project directory:

```bash
cd schoolsmis/
```
* Install the requirements by selecting where you want to run (base, developement, production):

```bash
pip install -r requirements.txt
```

*PS: If you have issues installing either `gunicorn` or `psycopg2`, you can remove them from the requirements.txt file and run the command again.*

* Create the database:

```bash
python manage.py migrate
```

* Enter inside the grs-react app:

```bash
cd schoolmis/grs-react/
```
* Run the following command to install the node modules:

```bash
npm install
```
* Build the javascript files needed for deployment using the following command:

```bash
npm run build
```
* Run collectstatic after you build the js files using the following command:

```bash
python manage.py collectstatic
```
* Finally run the django server using production settings and you are good to go:

```bash
python manage.py runserver --settings=schoolmis.settings.production
```

The project will be available at **127.0.0.1:8000**.
