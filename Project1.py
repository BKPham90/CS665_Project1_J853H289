import sqlite3

from tkinter import *
from DatabaseController import *

controller = DatabaseController(sqlite3.connect("GA_Maintenance.db"))

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
    command = lambda: controller.DisplayAirplanes(dataTextBox)
)
displayAirplanesBtn.pack()

displayMechanicsBtn = Button(
    window,
    text = "Display Mechanics",
    command = lambda: controller.DisplayMechanics(dataTextBox)
)
displayMechanicsBtn.pack()

displayPartsBtn = Button(
    window,
    text = "Display Parts",
    command = lambda: controller.DisplayParts(dataTextBox)
)
displayPartsBtn.pack()

displayServices = Button(
    window,
    text = "Display Services",
    command = lambda: controller.DisplayServices(dataTextBox)
)
displayServices.pack()

deleteTableLabel = Label(window, text = "Enter table to delete from:")
deleteTableLabel.pack()

deleteTableEntry = Entry(window)
deleteTableEntry.pack()

deleteIdLabel = Label(window, text = "Enter id of record to delete:")
deleteIdLabel.pack()

deleteIdEntry = Entry(window)
deleteIdEntry.pack()

deleteRecordButton = Button(
    window,
    text = "Delete Record",
    command = lambda: controller.DeleteRecord(deleteTableEntry.get(), deleteIdEntry.get())
)
deleteRecordButton.pack()

window.mainloop()

controller.connection.close()