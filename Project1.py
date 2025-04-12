import sqlite3
import DatabaseController

from DataDisplayControl import *
from DeleteControl import *
from UpdateControl import *

from tkinter import *

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

DataDisplay = DataDisplayControl(window)
Deleter = DeleteControl(window)
Updater = UpdateControl(window)

createTableLabel = Label(window, text = "Enter table for new record:")
createTableLabel.pack()

createTableEntry = Entry(window)
createTableEntry.pack()

createDataLabel = Label(window, text = "Enter data for new record separated by commas:")
createDataLabel.pack()

createDataEntry = Entry(window)
createDataEntry.pack()

createTableButton = Button(
    window,
    text = "Create New Record",
    command = lambda: DatabaseController.CreateNewRecord(createTableEntry.get(), createDataEntry.get())
)
createTableButton.pack()

window.mainloop()

DatabaseController.Connection.close()