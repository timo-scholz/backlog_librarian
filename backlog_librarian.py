import create_db
import database_handler
import os
from steam import steamUser
from gog import gogUser




def readUserData(filename = "userdata.txt"):
    Data = []
    with open(filename) as userData:
        for line in userData:
            Data.append(line.split("="))

    return Data

def userdataexists():
    if not os.path.isfile("userdata.txt"):
        with open('userdata.txt', 'w') as f:
            f.write('STEAMID64=ID64_HERE\nSTEAM_APIKEY=APIKEY_HERE')


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
        image = str(x["image"])
        steamData.insert_game(game_id, name, 0, 1, 0, image)

    #steamData.print_games()


def getGogGames():
    #todo Auth Method should ask for logins here

    guser = gogUser()


    gogGames = guser.getGames()

    gogData = database_handler.Game('gog.db')

    for x in gogGames:
        values = x.values()
        game_id = int(x["id"])
        name = str(x["name"]),
        image = str(x["image"])
        split_name = str(name).split("'")
        gogData.insert_game(game_id, split_name[1], 0, 2, 0, image)

    print(len(gogGames))

def mergeIntoOwned():
    print("cool")
    #TODO merging databases into owned.db
    

def main():
    userdataexists()
    create_db.main()
    #getSteamGames()
    #getGogGames()

    

main()