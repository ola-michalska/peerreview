# Library Booking System

In order to start the system please first run the SQL query in the file 'assignment_4_sql_query'

Once this is done, please change the config file to reflect your credentials:
- leave the DATABASE as is, this reflects the name from SQL query
- you can find your HOST and USER credentials in SQL Workbench (Database -> Manage Connections)
- your password is private

Install the following dependencies:
1. requests
2. Flask
3. mysql-connector-python
4. prettytable

You can do this by running 
`pip install requests flask mysql-connector-python prettytable`

Please run the files as follows:

1. db_utils.py
2. app.py
3. main.py

this will start the console app.

The system has the following features:

1. Add new account
2. Delete account
3. Browse book sections by:
   - title
   - genre
   - author
   - view all
4. Add book to account
5. View currently rented book
6. Return a book
