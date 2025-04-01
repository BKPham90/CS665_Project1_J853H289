import sqlite3

from tkinter import *

connection = sqlite3.connect("GA_Maintenance.db")
cursor = connection.cursor()

createFile = open("create.sql", "r")
createCommands = createFile.read().split(';')
createFile.close()
for createCommand in createCommands:
    cursor.execute(createCommand)
    connection.commit()

insertFile = open("insert.sql", "r")
insertCommands = insertFile.read().split(';')
insertFile.close()
for insertCommand in insertCommands:
    cursor.execute(insertCommand)
    connection.commit()

crudFile = open("crud.sql", "r")
crudCommands = crudFile.read().split(';')
crudFile.close()
for crudCommand in crudCommands:
    cursor.execute(crudCommand)
    connection.commit()