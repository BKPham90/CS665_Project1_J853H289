import sqlite3

from tkinter import *

Connection = sqlite3.connect("GA_Maintenance.db")
Cursor = Connection.cursor()

FieldNameLookup = {
        "Airplanes": ("tail_number", "make", "model", "year"),
        "Mechanics": ("mechanic_id", "first_name", "last_name", "certifaction_last_renewed"),
        "Parts": ("part_id", "part_name", "vendor_name", "airworthiness_certified"),
        "Services": ("service_id", "service_description", "service_date", "tail_number", "part_id", "mechanic_id")
}

def DisplayAirplanes(outputTextBox: Text):
    outputTextBox.delete('1.0', END)
    Cursor.execute(
        """
        SELECT *
        FROM Airplanes
        ORDER BY tail_number
        """
    )
    results = Cursor.fetchall()
    for columnName in FieldNameLookup["Airplanes"]:
        outputTextBox.insert(END, columnName)
        outputTextBox.insert(END, " |\t")
    outputTextBox.insert(END,f"\n{"-" * 40}\n")
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")

def DisplayMechanics(outputTextBox: Text):
    outputTextBox.delete('1.0', END)
    Cursor.execute(
        """
        SELECT *
        FROM Mechanics
        ORDER BY mechanic_id
        """
    )
    results = Cursor.fetchall()
    for columnName in FieldNameLookup["Mechanics"]:
        outputTextBox.insert(END, columnName)
        outputTextBox.insert(END, " |\t")
    outputTextBox.insert(END,f"\n{"-" * 40}\n")
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")

def DisplayParts(outputTextBox: Text):
    outputTextBox.delete('1.0', END)
    Cursor.execute(
        """
        SELECT *
        FROM Parts
        ORDER BY part_id
        """
    )
    results = Cursor.fetchall()
    for columnName in FieldNameLookup["Parts"]:
        outputTextBox.insert(END, columnName)
        outputTextBox.insert(END, " |\t")
    outputTextBox.insert(END,f"\n{"-" * 40}\n")
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")

def DisplayServices(outputTextBox: Text):
    outputTextBox.delete('1.0', END)
    Cursor.execute(
        """
        SELECT *
        FROM Services
        ORDER BY service_id
        """
    )
    results = Cursor.fetchall()
    for columnName in FieldNameLookup["Services"]:
        outputTextBox.insert(END, columnName)
        outputTextBox.insert(END, " |\t")
    outputTextBox.insert(END,f"\n{"-" * 40}\n")
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")

def DeleteRecord(fromTable: str, id):
    idName = FieldNameLookup[fromTable][0]
    if type(id) == str: id = f"'{id}'"
    if idName != "Unknown Table":
        Cursor.execute(
            f"""
            DELETE FROM {fromTable}
            WHERE {idName} = {id}
            """
        )
        Connection.commit()

def UpdateRecord(fromTable: str, id, property: str, newValue):
    idName = FieldNameLookup[fromTable][0]
    if type(id) == str: id = f"'{id}'"
    if type(newValue) == str: newValue = f"'{newValue}'"
    if idName != "Unknown Table":
        Cursor.execute(
            f"""
            UPDATE {fromTable}
            SET {property} = {newValue}
            WHERE {idName} = {id}
            """
        )
        Connection.commit()

def CreateNewRecord(toTable: str, data: str):
    columns = ", ".join(FieldNameLookup[toTable])
    Cursor.execute(
        f"""
        INSERT INTO {toTable} ({columns})
        VALUES ({data})
        """
    )
    Connection.commit()

def DisplayServicesForAirplane(outputTextBox: Text, tail_number: str):
    outputTextBox.delete('1.0', END)
    Cursor.execute(
        f"""
        SELECT *
        FROM Services
        WHERE tail_number = '{tail_number}'
        ORDER BY service_date
        """
    )
    results = Cursor.fetchall()
    for columnName in FieldNameLookup["Services"]:
        outputTextBox.insert(END, columnName)
        outputTextBox.insert(END, " |\t")
    outputTextBox.insert(END,f"\n{"-" * 40}\n")
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")

def DisplayServicesForMechanic(outputTextBox: Text, mechanic_id: int):
    outputTextBox.delete('1.0', END)
    Cursor.execute(
        f"""
        SELECT *
        FROM Services
        WHERE mechanic_id = {mechanic_id}
        ORDER BY service_date
        """
    )
    results = Cursor.fetchall()
    for columnName in FieldNameLookup["Services"]:
        outputTextBox.insert(END, columnName)
        outputTextBox.insert(END, " |\t")
    outputTextBox.insert(END,f"\n{"-" * 40}\n")
    for row in results:
        for column in row:
            outputTextBox.insert(END, column)
            outputTextBox.insert(END, "\t")
        outputTextBox.insert(END, "\n")