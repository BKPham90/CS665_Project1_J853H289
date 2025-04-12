import sqlite3
import DatabaseController

from DataDisplayControl import *
from DeleteControl import *
from UpdateControl import *
from CreateControl import *

from tkinter import *

window = Tk()
window.title("General Aviation Maintence")

DataDisplay = DataDisplayControl(window)
Deleter = DeleteControl(window)
Updater = UpdateControl(window)
Creator = CreateControl(window)

window.mainloop()

DatabaseController.Connection.close()