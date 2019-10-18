import os
import json
import shutil


def pega_top_jogos(fileOut):
    os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/games/top' > "+fileOut)


def pega_stream_jogos(nome, id):

    os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/streams?first=20&game_id=" +
              id+"' > streams/" + file_string(nome)+".json")



def pega_b(nome, id):
    # https://api.twitch.tv/helix/users?id=44322889
    os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/users?login=beethoven1997' > beethoven.json")


def pega_streamers(nome, id,game_name):
    # https://api.twitch.tv/helix/users?id=44322889
    filepath=id+"' > "+game_name+"/" + file_string(nome)+".json"
    os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/users?id="+filepath )


def file_string(str):
    return str.replace(" ", "").replace('&', "").replace("'", "")



def pega_follow(nome,id):
    os.system("curl -H 'Client-ID: ioe7gqjfxhbxr0aqg4drweoul0jtrt' -X GET 'https://api.twitch.tv/helix/users/follows?from_id=" +
              id+"' >" + file_string(nome)+".json")





def genarateDataBase():
            
    shutil.rmtree('users')
    shutil.rmtree('streams')
    os.makedirs('users')
    os.makedirs('streams')
    #Adiciona um dicionario com os jogos mais assistidos,e cria varios os dicionarios com as top strems desse jogo
    pega_top_jogos("topJogos")
    with open("top_Jogos.json") as json_file:
        data = json.load(json_file)

    for i in range(len(data['data'])):
        path="users/"+file_string(data["data"][i]["name"])
        if not os.path.exists(path):
            os.makedirs(path)
        name=data["data"][i]["name"]
        idG=data["data"][i]["id"]
        pega_stream_jogos(name,idG)

        with open("streams/"+file_string(data['data'][i]['name']+".json")) as json_file:
            data_stream = json.load(json_file)

        for j in range(len(data_stream['data'])):

            path_user=path+"/"+file_string(data_stream['data'][j]['user_name'])
            if not os.path.exists(path_user):
                os.makedirs(path_user)

            pega_streamers(data_stream['data'][j]['user_name'],
            data_stream['data'][j]['user_id'],file_string(path_user))

            with open(path_user+"/"+file_string(data_stream['data'][j]['user_name']+".json")) as json_file:
                data_streamer = json.load(json_file)

                
            for k in range(len(data_streamer['data'])):
                followPath=path_user
                name=data_streamer["data"][k]["login"]
                pega_follow(followPath+"/"+name+"Follows",data_streamer["data"][k]["id"])

                






#pega_stream_jogos("testeee","493057")
genarateDataBase()