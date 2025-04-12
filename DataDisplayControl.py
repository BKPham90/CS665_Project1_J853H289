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

        self.BottomBar = Frame(self.ControlFrame)
        self.BottomBar.pack()

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

        self.DisplayServicesForAirplaneEntry = Entry(self.BottomBar)
        self.DisplayServicesForAirplaneEntry.grid(row=1, column=0)

        self.DisplayServicesForAirplaneBtn = Button(
            self.BottomBar,
            text = "Show Services for Airplane Id:",
            command = lambda: DatabaseController.DisplayServicesForAirplane(
                self.DataDisplay,
                self.DisplayServicesForAirplaneEntry.get()
            )
        )
        self.DisplayServicesForAirplaneBtn.grid(row=0, column=0)

        self.DisplayServicesForMechanicEntry = Entry(self.BottomBar)
        self.DisplayServicesForMechanicEntry.grid(row=1, column=1)

        self.DisplayServicesForMechanicBtn = Button(
            self.BottomBar,
            text = "Show Services for Mechanic Id:",
            command = lambda: DatabaseController.DisplayServicesForMechanic(
                self.DataDisplay,
                self.DisplayServicesForMechanicEntry.get()
            )
        )
        self.DisplayServicesForMechanicBtn.grid(row=0, column=1)