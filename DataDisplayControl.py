import DatabaseController

from tkinter import *

class DataDisplayControl:
    
    def __init__(self, parent):
        self.ControlFrame = Frame(parent)
        self.ControlFrame.pack()

        self.TopBar = Frame(self.ControlFrame)
        self.TopBar.pack()

        self.DataDisplay = Text(self.ControlFrame)
        self.DataDisplay.pack()

        self.DisplayAirplanesBtn = Button(
            self.TopBar,
            text = "Display Airplanes",
            command = lambda: DatabaseController.DisplayAirplanes(self.DataDisplay)
        )
        self.DisplayAirplanesBtn.pack(side="left")

        self.DisplayMechanicsBtn = Button(
            self.TopBar,
            text = "Display Mechanics",
            command = lambda: DatabaseController.DisplayMechanics(self.DataDisplay)
        )
        self.DisplayMechanicsBtn.pack(side="left")

        self.DisplayPartsBtn = Button(
            self.TopBar,
            text = "Display Parts",
            command = lambda: DatabaseController.DisplayParts(self.DataDisplay)
        )
        self.DisplayPartsBtn.pack(side="left")
        
        self.DisplayServicesBtn = Button(
            self.TopBar,
            text = "Display Services",
            command = lambda: DatabaseController.DisplayServices(self.DataDisplay)
        )
        self.DisplayServicesBtn.pack(side="left")