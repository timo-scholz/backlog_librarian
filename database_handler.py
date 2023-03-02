import sqlite3

class Game:

    # Constructor of Game
    # Arguments:
    # pDatabase: String of Path to Database
    def __init__(self, pDatabase, id_number=-1, name="", status=-1, plattform=-1, rating=-1, image=-1):
        self.id_number = id_number
        self.name = name
        self.status = status
        self.plattform = plattform
        self.rating = rating
        self.image = image
        self.connection = sqlite3.connect(pDatabase)
        self.cursor = self.connection.cursor()

    # Function to load entry
    def load_game(self, pId_number):
        self.cursor.execute("""
        SELECT * FROM games
        WHERE id = {}
        """.format(pId_number))

        results = self.cursor.fetchone()

        self.id_number = pId_number
        self.name = results[1]
        self.status = results[2]
        self.plattform = results[3]
        self.rating = results[4]
        self.image = results[5]

    # Function to insert row
    def insert_game(self, pId_number, pName, pStatus, pPlattform, pRating, pImage):
        illegalApo = pName.count("'")

        if illegalApo > 0:
            x = pName.split("'")
            pName = ""
            for y in x:
                pName = pName + y + "''"

        self.cursor.execute("""
        INSERT INTO games VALUES
        ({}, '{}', {}, {}, {}, {})
        """.format(pId_number, pName, pStatus, pPlattform, pRating, pImage))

        self.connection.commit()

    # Function to set Rating
    def set_rating(self, pId_number, pRating):
        self.cursor.execute("""
        UPDATE games
        SET rating = {}
        WHERE id = {}
        """.format(pRating, pId_number))

        self.connection.commit()

    # Function to set Status
    def set_status(self, pId_number, pStatus):
        self.cursor.execute("""
        UPDATE games
        SET status = {}
        WHERE id = {}
        """.format(pStatus, pId_number))

        self.connection.commit()

    # Function to set Plattform
    def set_plattform(self, pId_number, pPlattform):
        self.cursor.execute("""
        UPDATE games
        SET plattform = {}
        WHERE id = {}
        """.format(pPlattform, pId_number))

        self.connection.commit()

    # Function to print row
    def print_game(self, pId_number):
        self.load_game(pId_number)
        print(self.name)
        print(self.status)
        print(self.plattform)
        print(self.rating)
        print(self.image)

    # Function to alle rows
    def print_games(self):
        self.cursor.execute("""
        SELECT * FROM games
        """.format())

        results = self.cursor.fetchall()
        print(results)