from sqlite3 import *
from tkinter import *

class DatabaseController:

    def __init__(self, connection: Connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.fieldNameLookup = {
                "Airplanes": ("tail_number", "make", "model", "year"),
                "Mechanics": ("mechanic_id", "first_name", "last_name", "certifaction_last_renewed"),
                "Parts": ("part_id", "part_name", "vendor_name", "airworthiness_certified"),
                "Services": ("service_id", "service_description", "service_date", "tail_number", "part_id", "mechanic_id")
        }

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

    def DeleteRecord(self, fromTable: str, id):
        idName = self.fieldNameLookup[fromTable][0]
        if type(id) == str: id = f"'{id}'"
        if idName != "Unknown Table":
            self.cursor.execute(
                f"""
                DELETE FROM {fromTable}
                WHERE {idName} = {id}
                """
            )
            self.connection.commit()
    
    def UpdateRecord(self, fromTable: str, id, property: str, newValue):
        idName = self.fieldNameLookup[fromTable][0]
        if type(id) == str: id = f"'{id}'"
        if type(newValue) == str: newValue = f"'{newValue}'"
        if idName != "Unknown Table":
            self.cursor.execute(
                f"""
                UPDATE {fromTable}
                SET {property} = {newValue}
                WHERE {idName} = {id}
                """
            )
            self.connection.commit()
    
    def CreateNewRecord(self, toTable: str, data: str):
        columns = ", ".join(self.fieldNameLookup[toTable])
        self.cursor.execute(
            f"""
            INSERT INTO {toTable} ({columns})
            VALUES ({data})
            """
        )
        self.connection.commit()