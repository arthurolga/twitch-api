import requests
import json
import schedule
from datetime import datetime
import time
from library import *

#'2008-01-01 00:00:01'
games_ids={
    #Call of Duty: Modern Warfare
    "Call of Duty: Modern Warfare":"512710",
    #Fortnite 
    "Fortnite":"33214",
    #League of Legends
    "League of Legends":"21779",
    #Just Chatting 
    "Just Chatting":"509658",
    #Grand Theft Auto V
    "Grand Theft Auto V":"32982", 
    #Counter-Strike: Global Offensive 
    "Counter-Strike: Global Offensive":"32399",
    #Dead by Daylight
    "Dead by Daylight":"491487" ,
    #Apex Legends
    "Apex Legends":"511224", 
    #Teamfight Tactics
    "Teamfight Tactics":"513143",
    #World of Warcraft 
    "World of Warcraft ":"18122" 
}




headers = {'content-type': 'application/json',
'Client-ID': 'ioe7gqjfxhbxr0aqg4drweoul0jtrt'}





def GetGameData(game_id):
    url="https://api.twitch.tv/helix/games"
    para={"id":game_id}
    response = requests.get(url,headers=headers,params=para)
    response = response.json()["data"]
    
    return response



def FillGameDataBase():
    for i in games_ids:
        response=GetGameData(games_ids[i])
        name=response[0]["name"]
        game_id=response[0]["id"]
        add_game(conn,name,game_id)


def GetStreamerData(streamer_id):
    url='https://api.twitch.tv/helix/users'
    para={"id":streamer_id}
    response = requests.get(url,headers=headers,params=para)
    response = response.json()["data"]

    return response


def addStreamertoDataBase(streamer_id):
    response=GetStreamerData(streamer_id)
    streamer_id = response[0]["id"]
    login = response[0]["login"]
    display_name = response[0]["display_name"]
    streamer_type = response[0]["type"]
    broadcaster_type = response[0]["broadcaster_type"]
    profileImageURL = response[0]["profile_image_url"]
    view_count = response[0]["view_count"]
    add_Streamer(conn,streamer_id,login,display_name,streamer_type,broadcaster_type,profileImageURL,view_count)


def GetTopStreamsbyGame(game_id):
    url='https://api.twitch.tv/helix/streams'
    para={"first":"50",
        "game_id":game_id}
    response = requests.get(url,headers=headers,params=para)
    response=response.json()["data"]
    print(response)

    return response

def addStreamtoDataBase():
    for j in games_ids:
        response=GetTopStreamsbyGame(games_ids[j])
        for i in range(len(response)):
            id=response[i]["id"]
            user_id=response[i]["user_id"]
            user_name=response[i]["user_name"]
            game_id=response[i]["game_id"]
            type=response[i]["type"]
            title=response[i]["title"]
            viewer_count=response[i]["viewer_count"]
            started_at=response[i]["started_at"]
            request_time=datetime.now()
            language=response[i]["language"]
            addStreamertoDataBase(user_id)
            add_stream(conn,id,user_id,user_name,game_id,type,title,viewer_count,started_at,request_time,language)


def get_link(from_id,to_id):
    url = "https://api.twitch.tv/helix/users/follows?from_id="+from_id+"&to_id="+to_id
    headers = {'content-type': 'application/json',
'Client-ID': 'ioe7gqjfxhbxr0aqg4drweoul0jtrt'}
    response = requests.get(url,headers=headers)
    response = response.json()["data"]
    return response

def fillUserLinks():

    for game_name in games_ids:
        id=games_ids[game_name]
        streamer_ids=list_user_id_game(conn,id)
        for i in range(len(streamer_ids)):
            for j in range(len(streamer_ids)):
                req = get_link(str(streamer_ids[i][0]),str(streamer_ids[j][0]))
                if len(req)>0:
                    print(game_name,streamer_ids[i][0],streamer_ids[j][0])
                    add_link(conn,game_name,streamer_ids[i][0],streamer_ids[j][0])

        #print(streamer_ids)


#FillGameDataBase()
#addStreamtoDataBase()

#fillUserLinks()

conn.close()
    