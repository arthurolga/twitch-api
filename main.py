import os
import json


def pega_top_jogos(fileOut):
    os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/games/top' > "+fileOut)


def pega_stream_jogos(nome, id):
    os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/streams?first=20&game_id=" +
              id+"' > jogos/" + file_string(nome)+".json")


def pega_streamers(nome, id):
    # https://api.twitch.tv/helix/users?id=44322889
    os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/users?id=" +
              id+"' > users/" + file_string(nome)+".json")


def file_string(str):
    return str.replace(" ", "").replace('&', "").replace("'", "")


# os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/games/top' > topgames.json")
games = "top_jogos.json"

pega_top_jogos(games)

with open(games) as json_file:
    data = json.load(json_file)

for i in range(len(data['data'])):
    # print(data['data'][0]['id'])
    print(data['data'][i]['name'])
    pega_stream_jogos(data['data'][i]['name'], data['data'][i]['id'])

    # Le nome_do_jogo.json
    with open("jogos/"+file_string(data['data'][i]['name']+".json")) as json_file:
        data_jogo = json.load(json_file)

    for j in range(len(data_jogo)):
        print(data_jogo['data'][j]['user_name'])
        pega_streamers(data_jogo['data'][j]['user_name'],
                       data_jogo['data'][j]['user_id'])


# os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/games/top' > topgames1.json")
