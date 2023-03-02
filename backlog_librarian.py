import create_db
import database_handler
from steam import steamUser


create_db.main()

#database_handler.insert_game(self, 1, "TEXT", 1, 2, 3, 4)


# Credits for steam.py go to https://github.com/zeo/python-steamuser
def getSteamGames():
    # Set Steam ID and API Key
    user = steamUser("STEAMID64", "APIKEY")
    steamGames = user.getGames()
    length = len(steamGames)

    #
    steamData = database_handler.Game('steam.db')

    for x in steamGames:
        values = x.values()
        game_id = int(x["id"])
        name = str(x["name"])
        steamData.insert_game(game_id, name, 0, 1, 0, game_id)

    steamData.print_games()

#getSteamGames()

steamData = database_handler.Game('steam.db')
steamData.print_games()