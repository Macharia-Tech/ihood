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



## User Stories
The application user is able to:
- Create an account and confirm through email verification.
- Sign in to the application to start using.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Search for Neighbourhoods
- Only view details of a single neighborhood.
- View my profile page.
     

## Technologies Used
- Python 3.6.6(Django Framework)
- HTML5
- CSS3
- Bootstrap4
- Postgresql
- Heroku(Deployment)
- Visual Studio Code text editor     


## Known Bugs
No known bugs so far.Contact me if you come across any @ mitchelaudrey@gmail.com


## Support and Contact Details
For any comments,suggestions,feedback or inquiries about my application,Contact me via email:giftlumumba2@gmail.com
