# importing 'database' py file as 'db'
import database.database as db
# importing / using dotenv for storing login data locally
import os
from dotenv import load_dotenv

import wx
import wx.grid
from gui.app import TableViewer

load_dotenv()

# database config
host = os.getenv('HOST')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
database_name = os.getenv('DATABASE')

if __name__ == "__main__":  
    # create database connection object
    database = db.DataBase(host, username, password, database_name)
    # creating an instance with no redirecting of output or error
    app = wx.App(False)
    # instantiate the TableViewer class from app.py
    frame = TableViewer(None, "Database Tables", database)

    app.MainLoop()
    database.disconnect()
else:
    print("Something went wrong. Try again later!")
