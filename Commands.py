from sqlite3 import *
from tkinter import *

def DisplayAirplanes(cursor: Cursor, outputTextBox: Text):
    outputTextBox.delete('1.0', END)
    cursor.execute(
        """
        SELECT *
        FROM Airplanes
        ORDER BY tail_number
        """
    )
    results = cursor.fetchall()
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")

def DisplayMechanics(cursor: Cursor, outputTextBox: Text):
    outputTextBox.delete('1.0', END)
    cursor.execute(
        """
        SELECT *
        FROM Mechanics
        ORDER BY mechanic_id
        """
    )
    results = cursor.fetchall()
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")

def DisplayParts(cursor: Cursor, outputTextBox: Text):
    outputTextBox.delete('1.0', END)
    cursor.execute(
        """
        SELECT *
        FROM Parts
        ORDER BY part_id
        """
    )
    results = cursor.fetchall()
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")

def DisplayServices(cursor: Cursor, outputTextBox: Text):
    outputTextBox.delete('1.0', END)
    cursor.execute(
        """
        SELECT *
        FROM Services
        ORDER BY service_id
        """
    )
    results = cursor.fetchall()
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")