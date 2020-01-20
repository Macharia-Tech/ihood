# Ihood

 This is a web application that allows one to be in the loop about everything happening in his/her neighborhood from contact information of different meeting announcements or even alerts.This application was created on 19th January 2020

 # Author
Audrey Macharia


## Setup and installation

- Clone the Repo uding the following command:
  `git clone https://github.com/AudreyCherrie/Ihood.git`
- Activate virtual environment using python3.6 as default handler by running 
    `python3.6 -m venv virtual` then enter the virtual environment using `source virtual/bin/activate`
- Download the latest version of pip in the virtual environment: `$ curl https://bootstrap.pypa.io/get-pip.py | python`

- Install all application dependancies 
`pip install -r requirements.txt`

- Create the Database
    -On the terminal,run `psql`
    - Create a database by typing 
      `CREATE DATABASE hood;` for example.

- Create a .env file and add the following:

    - SECRET_KEY = `<Secret_key>`
    - DB_NAME = `awards`
    - DB_USER = `<Username>`
    - DB_PASSWORD = `your db password`
    - DEBUG = `True`

- Run Initial Migration
    `python3.6 manage.py makemigrations <name of the app>`
    `python3.6 manage.py migrate`

- Run the app
    `python3.6 manage.py runserver`
    `Open terminal on localhost:8000