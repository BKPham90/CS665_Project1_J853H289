import sqlite3

from tkinter import *
from Commands import *

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

displayAirplanesBtn = Button(
    window,
    text = "Display Airplanes",
    command = lambda: DisplayAirplanes(cursor, dataTextBox)
)
displayAirplanesBtn.pack()

displayMechanicsBtn = Button(
    window,
    text = "Display Mechanics",
    command = lambda: DisplayMechanics(cursor, dataTextBox)
)
displayMechanicsBtn.pack()

displayPartsBtn = Button(
    window,
    text = "Display Parts",
    command = lambda: DisplayParts(cursor, dataTextBox)
)
displayPartsBtn.pack()

displayServices = Button(
    window,
    text = "Display Services",
    command = lambda: DisplayServices(cursor, dataTextBox)
)
displayServices.pack()

window.mainloop()

connection.close()