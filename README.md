# Guess My Number Game

## Table of Contents

- [Introduction](#introduction)
- [Process and Information Flow Analysis](#process-and-information-flow-analysis)
- [Document Analysis](#document-analysis)
- [Conceptual Model](#conceptual-model)
- [Implementation Requirements](#implementation-requirements)

## Introduction

This project presents the implementation of the "Guess My Number" game, which uses a graphical user interface (GUI) developed in the Python programming language, with data stored in an SQL Server database. Users enter their nickname and try to guess a randomly generated number, and the results are saved and can be reviewed within the application.

## Process and Information Flow Analysis

The "Guess My Number" game process includes the following steps:

- **User Entry:** The user enters their username in the application's initial window. If the user does not enter a nickname, the nickname "Guest" is automatically assigned.
- **Username Check:** The application checks whether the username already exists in the database. If it does, the user must enter a new name.
- **Game Play:** Upon successful username entry, the game starts, where the user attempts to guess the randomly generated number in as few tries as possible.
- **Saving Results:** Upon game completion, the application saves the user's result (nickname, number of attempts, time taken to guess, date) into the database.
- **Viewing Results:** The user can review all previous results through the graphical interface.

## Document Analysis

The following documents were used for the development of this application:

- Technical documentation for the `pyodbc` module, which enables the connection of the Python application to the SQL Server database.
- Documentation for the `tkinter` module, used for creating the graphical user interface in Python.
- Specifications for SQL Server and T-SQL queries, used for creating and manipulating data in the database.

## Conceptual Model

The conceptual model of the database includes one table, `Scores`, which contains the following columns:

- `Username` (nvarchar): The user's name.
- `Attempts` (int): The number of attempts the user made.
- `TimeTaken` (float): The time taken to guess the number, rounded to two decimal places.
- `DatePlayed` (datetime): The date and time when the game was played.

## Implementation Requirements

- Python 3.x with the following installed modules: `tkinter`, `pyodbc`, `random`, `time`.
- Installed SQL Server with a created database `GuessNumberDB` and a `Scores` table.
- ODBC driver for SQL Server configured on the computer.
