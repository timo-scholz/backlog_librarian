import requests

BASE_URL = "http://api.steampowered.com/"
USER_URL = BASE_URL + "ISteamUser/GetPlayerSummaries/v0002/"
GAME_URL = BASE_URL + "IPlayerService/GetOwnedGames/v0001/"
BAN_URL  = BASE_URL + "ISteamUser/GetPlayerBans/v1/"

class steamUser:
    def __init__(self, steamid, apiKey):
        self.steamid = steamid
        self.apikey = apiKey

    # Function to convert SteamID64 to SteamID
    # Credits go to https://gist.github.com/bcahue/4eae86ae1d10364bb66d
    def transformSteamID(self):
        steamid64ident = 76561197960265728

        steamid = []
        steamid.append('STEAM_0:')
        steamidacct = int(self.steamid) - steamid64ident
        
        if steamidacct % 2 == 0:
            steamid.append('0:')
        else:
            steamid.append('1:')
        
        steamid.append(str(steamidacct // 2))
        
        return ''.join(steamid)

    # Function:  getUser()
    # Arguments: null
    # Returns:   user: Dictionary
    def getUser(self):
        request = requests.get(USER_URL + "?key=" + self.apikey + "&steamids=" + self.steamid)
        response = request.json()
        data = response["response"]["players"][0]

        user = {
            "name": data["personaname"],
            "steamid": self.transformSteamID(),
            "steamid64": data["steamid"],
            "profileurl": data["profileurl"],
            "onlinestate": self.getProfileState(data["profilestate"]),
            "visibilityState": self.getVisibilityState(data["communityvisibilitystate"]),
            "avatars": {
                "normal": data["avatar"],
                "medium": data["avatarmedium"],
                "full": data["avatarfull"]
            }
        }

        return user

    # Function:  getGames()
    # Arguments: includeFree: Boolean
    # Returns:   gameCount: Integer, games: List
    def getGames(self, includeFree = False):
        includeFree = includeFree and "1" or "0"

        request = requests.get(GAME_URL + "?key=" + self.apikey + "&steamid=" + self.steamid + "&include_played_free_games=" + includeFree + "&include_appinfo=1")
        response = request.json()
        data = response["response"]

        

        if not data:
            return None, None

        games = []
        for game in data["games"]:
            gameObject = {
                "id": game["appid"],
                "name": game["name"],
                "image": "https://cdn.akamai.steamstatic.com/steam/apps/" + str(game["appid"]) + "/header.jpg" 
            }

            games.append(gameObject)

        return games