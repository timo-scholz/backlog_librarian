import sqlite3

 # Function to create Databases
def main():
    connection = sqlite3.connect('owned.db')

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    name TEXT,
    status INTEGR,
    plattform INTEGR,
    rating INTEGR,
    image INTEGR
    )
        """)

    connection.commit()
    connection.close()

    connection = sqlite3.connect('steam.db')

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    name TEXT,
    status INTEGR,
    plattform INTEGR,
    rating INTEGR,
    image INTEGR
    )
        """)

    connection.commit()
    connection.close()

    connection = sqlite3.connect('gog.db')

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    name TEXT,
    status INTEGR,
    plattform INTEGR,
    rating INTEGR,
    image INTEGR
    )
        """)

    connection.commit()
    connection.close()