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

updateTableLabel = Label(window, text = "Enter table make updates to:")
updateTableLabel.pack()

updateTableEntry = Entry(window)
updateTableEntry.pack()

updateIdLabel = Label(window, text = "Enter id of record to update:")
updateIdLabel.pack()

updateIdEntry = Entry(window)
updateIdEntry.pack()

updatePropertyLabel = Label(window, text = "Enter name of property to update:")
updatePropertyLabel.pack()

updatePropertyEntry = Entry(window)
updatePropertyEntry.pack()

updateValueLabel = Label(window, text = "Enter new value:")
updateValueLabel.pack()

updateValueEntry = Entry(window)
updateValueEntry.pack()

updateRecordButton = Button(
    window,
    text = "Update Record",
    command = lambda: controller.UpdateRecord(updateTableEntry.get(), updateIdEntry.get(), updatePropertyEntry.get(), updateValueEntry.get())
)
updateRecordButton.pack()

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
    command = lambda: controller.CreateNewRecord(createTableEntry.get(), createDataEntry.get())
)
createTableButton.pack()

window.mainloop()

controller.connection.close()