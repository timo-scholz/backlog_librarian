import create_db
import database_handler
from steam import steamUser




def readUserData(filename = "userdata.txt"):
    Data = []
    with open(filename) as userData:
        for line in userData:
            Data.append(line.split("="))

    return Data



# Credits for steam.py go to https://github.com/zeo/python-steamuser
def getSteamGames():
    # Set Steam ID and API Key
    uData = readUserData()
    user = steamUser(uData[0][1].strip('\n'), uData[1][1].strip('\n'))
    steamGames = user.getGames()

    steamData = database_handler.Game('steam.db')

    for x in steamGames:
        values = x.values()
        game_id = int(x["id"])
        name = str(x["name"])
        steamData.insert_game(game_id, name, 0, 1, 0, game_id)

    steamData.print_games()

def main():
    create_db.main()
    