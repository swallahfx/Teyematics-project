This Document is an API that can be used to:
1. Create New **Comments**
2. View **Posts based on Comments**

The function needed to Populate our database was written in the **views.py**: 
    this function made use of libraries like pandas to easily extract and loop through 
    all the contents of the csv files to populate our database. 

    N.B an If condition is set. in the function session of the file.This is to check
    wether the database has been populated already or not so there is a check and balance.

The Schema used to Create our database Table is written in the models.py N.B : It is a DjangoORM and
not an Sql query but they do exactly thesame thing.

The logic to search Comment by specified post is done by just filtering through the database tables

***To use this endpoint***

a. Copy or clone the project
b. Create a virtual environment Python3 -m venv venv
c. Activate the virtuL environment using source venv/bin/actvate 
d. Set-up your database using Postgresql in the settings.py
e. Input the necessary postgresql details then
f. run **python3 manage.py makemigrations** and **python3 manage.py migrate**
g. Pip install -r requirements.txt to install all the dependencies 
h. Python3 manage.py runserver
i. Ckick on:
    http://127.0.0.1:8000/api/v1/search/  :: to Search posts based on comments text
    http://127.0.0.1:8000/api/v1/add/comment/ :: to add a new comment


!See you.









