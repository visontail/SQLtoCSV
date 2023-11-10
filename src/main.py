# importing 'database' py file as 'db'
import database.database as db
# importing / using dotenv for storing login data locally
import os
from dotenv import load_dotenv

import wx
import wx.grid
from gui.app import DatabaseViewer

load_dotenv()

# database config
host = os.getenv('HOST')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')

if __name__ == "__main__":  
    # - create database connection object
    database = db.DataBase(host, username, password, database)
    # - connects to the db
    database.connect()
    #result = database.select_content('Sample1')
    #print(result)
    # print out tables
    tables = database.select_tables()
    for table in tables:
        print(table[0])

    app = wx.App(False)

    # Instantiate the DatabaseViewer class from app.py
    frame = DatabaseViewer(None, "Database Viewer", tables)

    app.MainLoop()

    # - disconnects from db
    database.disconnect()
else:
    print("Something went wrong. Try again later!")
