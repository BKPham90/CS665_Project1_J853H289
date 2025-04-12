import sqlite3

from tkinter import *
from DatabaseController import *

class TopBar:
    
    def __init__(self, parent):
        self.Frame = Frame(parent)

        self.DisplayAirplanesBtn = Button(
            window,
            text = "Display Airplanes",
            command = lambda: DatabaseController.DisplayAirplanes(dataTextBox)
        )
        displayAirplanesBtn.pack()
    