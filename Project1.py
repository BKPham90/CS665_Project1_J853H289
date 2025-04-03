import sqlite3

from tkinter import *

connection = sqlite3.connect("GA_Maintenance.db")
cursor = connection.cursor()

# createFile = open("create.sql", "r")
# createCommands = createFile.read().split(';')
# createFile.close()
# for createCommand in createCommands:
#     cursor.execute(createCommand)
#     connection.commit()

# insertFile = open("insert.sql", "r")
# insertCommands = insertFile.read().split(';')
# insertFile.close()
# for insertCommand in insertCommands:
#     cursor.execute(insertCommand)
#     connection.commit()

window = Tk()
window.title("General Aviation Maintence")

dataTextBox = Text(window)
dataTextBox.pack()

def displayData():
    cursor.execute("""
                   SELECT *
                   FROM Airplanes
                   ORDER BY tail_number
                   """
    )
    results = cursor.fetchall()
    for row in results:
        for column in row:
            dataTextBox.insert(END, column)
            dataTextBox.insert(END, "\t")
        dataTextBox.insert(END, "\n")

displayData()

window.mainloop()

connection.close()