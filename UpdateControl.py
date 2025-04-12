import DatabaseController

from tkinter import *

class UpdateControl:

    def __init__(self, parent):
        self.ControlFrame = Frame(parent)
        self.ControlFrame.pack()

        self.UpdateTableLabel = Label(
            self.ControlFrame,
            text = "Enter table make updates to:"
        )
        self.UpdateTableLabel.grid(row=0, column=0, sticky="e")

        self.UpdateTableEntry = Entry(self.ControlFrame)
        self.UpdateTableEntry.grid(row=0, column=1)

        self.UpdateIdLabel = Label(
            self.ControlFrame,
            text = "Enter id of record to update:"
        )
        self.UpdateIdLabel.grid(row=1, column=0, sticky="e")

        self.UpdateIdEntry = Entry(self.ControlFrame)
        self.UpdateIdEntry.grid(row=1, column=1)

        self.UpdatePropertyLabel = Label(
            self.ControlFrame,
            text = "Enter name of property to update:"
        )
        self.UpdatePropertyLabel.grid(row=2, column=0, sticky="e")

        self.UpdatePropertyEntry = Entry(self.ControlFrame)
        self.UpdatePropertyEntry.grid(row=2, column=1)

        self.UpdateValueLabel = Label(
            self.ControlFrame,
            text = "Enter new value:"
        )
        self.UpdateValueLabel.grid(row=3, column=0, sticky="e")

        self.UpdateValueEntry = Entry(self.ControlFrame)
        self.UpdateValueEntry.grid(row=3, column=1)

        self.UpdateRecordButton = Button(
            self.ControlFrame,
            text = "Update Record",
            command = lambda: DatabaseController.UpdateRecord(
                self.UpdateTableEntry.get(),
                self.UpdateIdEntry.get(),
                self.UpdatePropertyEntry.get(),
                self.UpdateValueEntry.get()
            )
        )
        self.UpdateRecordButton.grid(row=4, columnspan=2)