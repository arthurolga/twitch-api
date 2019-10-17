import os
import json
from sql import *

games = "gayes.json"

with open(games) as json_file:
    data = json.load(json_file)


# print(data['data'][0])
# criar_stream(connection, data['data'][0])
# print(games['top'])
for i in range(len(data['top'])):
    criar_game(connection, data['top'][i]['game'])

print("sepa foi")
