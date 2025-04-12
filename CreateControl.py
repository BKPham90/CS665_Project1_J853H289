import DatabaseController

from tkinter import *

class CreateControl:

    def __init__(self, parent):
        self.ControlFrame = Frame(parent)
        self.ControlFrame.pack()

        self.CreateTableLabel = Label(
            self.ControlFrame,
            text = "Enter table for new record:"
        )
        self.CreateTableLabel.grid(row=0, column=0, sticky="e")

        self.CreateTableEntry = Entry(self.ControlFrame)
        self.CreateTableEntry.grid(row=0, column=1)

        self.CreateDataLabel = Label(
            self.ControlFrame,
            text = "Enter data for new record separated by commas:"
        )
        self.CreateDataLabel.grid(row=1, column=0, sticky="e")

        self.CreateDataEntry = Entry(self.ControlFrame)
        self.CreateDataEntry.grid(row=1, column=1)

        self.CreateTableButton = Button(
            self.ControlFrame,
            text = "Create New Record",
            command = lambda: DatabaseController.CreateNewRecord(
                self.CreateTableEntry.get(),
                self.CreateDataEntry.get()
            )
        )
        self.CreateTableButton.grid(row=2, columnspan=2)