
import sqlite3
from datetime import datetime

def CreateDB(dataBaseFileName):

    conn = sqlite3.connect(dataBaseFileName)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE weights (username TEXT, weight REAL, date TEXT)') # Date will need to be stored as TEXT
    return cursor

def ConnectToDB(dataBaseFileName):

    conn = sqlite3.connect(dataBaseFileName)
    cursor = conn.cursor()
    return cursor

def LogWeightInDataBase(dataBaseFileName, jsonRequest):

    conn = sqlite3.connect(dataBaseFileName)
    cursor = conn.cursor()

    dateString = datetime.fromtimestamp(int(jsonRequest["date"]/1000)).strftime('%Y-%m-%d')
    print(f"User {jsonRequest["user"]} is {jsonRequest["weight"]} kg on date {dateString}")

    cursor.execute("""
                        INSERT INTO weights (username, weight, date)
                        VALUES (?, ?, ?)
                        """,
                   (
                                jsonRequest["user"],
                                jsonRequest["weight"],
                                dateString
                            )
                   )


    conn.commit()
    conn.close()

    print("Weight logged into database")


