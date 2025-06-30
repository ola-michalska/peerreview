# Hello there!

### I have created a simple application that allows user's to keep track of their favourite songs in rank. 
### Here are the instructions to get everything up and running!

1. Run the **create my_music_db_script.sql** in SQL workbench to create the db and associated table
2. Modify the **config.py** by adding your root SQL password to the password variable. These credentials allow you to set up an DB (**db_utils.py** defines SQL functions we'll use in our app)
3. Ensure the following dependencies are installed in your environment by running: pip install flask mysql-connector-python requests
4. Run the Flask application by running the **app.py** script - the server will start @ http://127.0.0.1:5000, establishing endpoints to manipulate your db
5. Then, run the client main.py to interact with the API, allowing you to view and modify your song rankings.

