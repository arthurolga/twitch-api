import pymysql
import subprocess
import unittest
import re

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='twitch',
    autocommit=True)


def add_Streamer(connection,streamer_id,login,display_name,streamer_type,broadcaster_type,profile_image,view_count):
    # nome, sobrenome, email, cidade
    query = """
    INSERT INTO streamer (streamer_id,streamer_login,streamer_display_name,streamer_type,streamer_broadcaster_type,streamer_profile_image_url,streamer_view_count) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    with conn.cursor() as cursor:
        try:
            cursor.execute(query,(streamer_id,login,display_name,streamer_type,broadcaster_type,profile_image,view_count))
            cursor.execute('COMMIT')
            print("Streamer adiocionado")
        except pymysql.err.IntegrityError as e:
            print("Usuario ja existente")



def add_stream(connection,stream_id,stream_user_id, stream_user_name, stream_game_id, stream_type,stream_title,stream_viewer_count,stream_started_at,stream_request_time,stream_language):
    # nome, sobrenome, email, cidade
    query = """
    INSERT INTO stream (stream_id,stream_user_id, stream_user_name, stream_game_id, stream_type,stream_title,stream_viewer_count,stream_started_at,stream_request_time,stream_language) 
    VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s,%s);
    """
    with conn.cursor() as cursor:
        try:
            cursor.execute(query,(stream_id,stream_user_id, stream_user_name,stream_game_id, stream_type,stream_title,stream_viewer_count,stream_started_at,stream_request_time,stream_language))
            cursor.execute('COMMIT')
            print("Stream adiocionado")
        except pymysql.err.IntegrityError as e:
            print("Stream ja existente")


def add_game(connection,game_name, game_id):
    query = """
    INSERT INTO game (game_name,game_id) 
    VALUES (%s, %s);
    """
    with conn.cursor() as cursor:
        try:
            cursor.execute(query,(game_name, game_id))
            cursor.execute('COMMIT')
        except pymysql.err.IntegrityError as e:
            print("Game ja existente")