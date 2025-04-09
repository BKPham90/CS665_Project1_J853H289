from sqlite3 import *
from tkinter import *

class DatabaseController:

    def __init__(self, connection: Connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def DisplayAirplanes(self, outputTextBox: Text):
        outputTextBox.delete('1.0', END)
        self.cursor.execute(
            """
            SELECT *
            FROM Airplanes
            ORDER BY tail_number
            """
        )
        results = self.cursor.fetchall()
        for row in results:
            for column in row:
                outputTextBox.insert(END, column)
                outputTextBox.insert(END, "\t")
            outputTextBox.insert(END, "\n")

    def DisplayMechanics(self, outputTextBox: Text):
        outputTextBox.delete('1.0', END)
        self.cursor.execute(
            """
            SELECT *
            FROM Mechanics
            ORDER BY mechanic_id
            """
        )
        results = self.cursor.fetchall()
        for row in results:
            for column in row:
                outputTextBox.insert(END, column)
                outputTextBox.insert(END, "\t")
            outputTextBox.insert(END, "\n")

    def DisplayParts(self, outputTextBox: Text):
        outputTextBox.delete('1.0', END)
        self.cursor.execute(
            """
            SELECT *
            FROM Parts
            ORDER BY part_id
            """
        )
        results = self.cursor.fetchall()
        for row in results:
            for column in row:
                outputTextBox.insert(END, column)
                outputTextBox.insert(END, "\t")
            outputTextBox.insert(END, "\n")

    def DisplayServices(self, outputTextBox: Text):
        outputTextBox.delete('1.0', END)
        self.cursor.execute(
            """
            SELECT *
            FROM Services
            ORDER BY service_id
            """
        )
        results = self.cursor.fetchall()
        for row in results:
            for column in row:
                outputTextBox.insert(END, column)
                outputTextBox.insert(END, "\t")
            outputTextBox.insert(END, "\n")

    def DeleteRecord(self, fromTable: str, id: str):
        idNameLookup = {
                "Airplanes": "tail_number",
                "Mechanics": "mechanic_id",
                "Parts": "part_id",
                "Services": "service_id"
        }
        idName = idNameLookup.get(fromTable, "Unknown Table")
        if idName != "Unknown Table":
            self.cursor.execute(
                f"""
                DELETE FROM {fromTable}
                WHERE {idName} = {id}
                """
            )
            self.connection.commit()