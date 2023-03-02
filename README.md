# Backlog Librarian

## WIP

App to manage Videogame Backlogs

Planned Features:

- completely local, no accounts
- automatically sync game entrys from plattforms like steam and gog (kinda done)
- gui
- game info from online database

## Steam

after the userdata.txt is generated fill in your STEAMID64 and an valid Steam API Key. the Rest is handled by the script

## GOG

until i or someone develops a cleaner version of this the workaround way for gog is to login your gog account in your browser and then save this json file https://embed.gog.com/account/getFilteredProducts?mediaType=1 into the root folder of this project

this works kinda unless you have only 100 games or less

in that case you can get the remaining pages by changing the page parameter like so: https://embed.gog.com/account/getFilteredProducts?mediaType=1&page=2

saving them like this works for now:
- getFilteredProducts0.json
- getFilteredProducts1.json
- ...
- getFilteredProductsX.json

the script reads all .json files named this way and adds the games to the database.

## Special Thanks
- https://github.com/zeo/python-steamuser
- https://gogapidocs.readthedocs.io/en/latest/
