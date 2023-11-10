# importing 'database' py file as 'db'
import database.database as db
# importing / using dotenv for storing login data locally
import os
from dotenv import load_dotenv

load_dotenv()

# database config
host = os.getenv('HOST')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')

if __name__ == "__main__":  
    # - create database connection object
    database = db.DataBase(host, username, password, database)
    # - connects to the database
    database.connect()
else:
    print("Something went wrong. Try again later!")

    