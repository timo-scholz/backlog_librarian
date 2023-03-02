import json

#def getJson():
    #TODO Auth

    #TODO download json file
    #https://embed.gog.com/account/getFilteredProducts?mediaType=1&page=2

    #check page in totalPages to download all json files


class gogUser:
    def __init__(self):
        self = self

    def getGames(self):
        ff = open('getFilteredProducts1.json')
        fdata = json.load(ff)
        pages = fdata["totalPages"]

        games = []
        ff.close()
        files = []
        products = []

        for x in range(pages):
            files.append('getFilteredProducts' + str(x) + '.json')

        for x in range(len(files)):
            openFile = open(str(files[x]))

        
            data = json.load(openFile)

            if not data:
                return None, None

            for game in data["products"]:
                gameObject = {
                    "id": game["id"],
                    "name": game["title"],
                    "image": "http:" + str(game["image"]) + ".jpg"
                }

                products.append(gameObject)

        return products