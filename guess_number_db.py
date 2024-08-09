import datetime

import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    r"Server=DESKTOP-2M280GH\SQLEXPRESS;"
    "Database=GuessNumberDB;"
    "Trusted_connection=yes;"
)


def save_score(username, attempts, time_taken):
    cursor = conn.cursor()

    time_taken = round(time_taken, 2)
    date = datetime.datetime.now().replace(microsecond=0)

    cursor.execute("INSERT INTO Scores (Username, Attempts, TimeTaken, DatePlayed)"
                   "VALUES (?, ?, ?, ?)", username, attempts, time_taken, date)

    cursor.commit()
    cursor.close()
