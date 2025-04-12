import DatabaseController

from tkinter import *

class DeleteControl:

    def __init__(self, parent):
        self.ControlFrame = Frame(parent)
        self.ControlFrame.pack()

        self.DeleteTableLabel = Label(
            self.ControlFrame,
            text = "Enter table to delete from:"
        )
        self.DeleteTableLabel.grid(row=0, column=0)

        self.DeleteTableEntry = Entry(self.ControlFrame)
        self.DeleteTableEntry.grid(row=0, column=1)

        self.DeleteIdLabel = Label(
            self.ControlFrame,
            text = "Enter id of record to delete:"
        )
        self.DeleteIdLabel.grid(row=1, column=0)

        self.DeleteIdEntry = Entry(self.ControlFrame)
        self.DeleteIdEntry.grid(row=1, column=1)

        self.DeleteRecordButton = Button(
            self.ControlFrame,
            text = "Delete Record",
            command = lambda: DatabaseController.DeleteRecord(
                self.DeleteTableEntry.get(),
                self.DeleteIdEntry.get()
            )
        )
        self.DeleteRecordButton.grid(row=2, columnspan=2)