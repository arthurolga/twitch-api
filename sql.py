import pymysql
import subprocess
import unittest
import re

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='twitch')


def criar_usuario1(connection, obj):
    # nome, sobrenome, email, cidade
    query = """
    INSERT INTO usuarios (nome, sobrenome, email, cidade) 
    VALUES (%s, %s, %s, %s);
    """

    with connection.cursor() as cursor:
        print('Executando query:')
        cursor.execute(
            query, (obj['nome'], obj['sobrenome'], obj['email'], obj['cidade']))
        cursor.execute('COMMIT')


def criar_stream(connection, obj):
    # nome, sobrenome, email, cidade
    query = """
    INSERT INTO stream (stream_id, stream_user_id, stream_user_name, stream_game_id, stream_type, stream_title, stream_viewer_count, stream_started_at, stream_language, stream_thumbnail_url, stream_tag_ids) 
    VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s,%s,%s);
    """

    with connection.cursor() as cursor:
        print('Executando query:')
        cursor.execute(
            query, (obj['id'], obj['user_id'], obj['user_name'], obj['game_id'], obj['type'], obj['title'], obj['viewer_count'], obj['started_at'], obj['language'], obj['thumbnail_url'], obj['tag_ids']))
        cursor.execute('COMMIT')


def criar_game(connection, obj):
    # game_name VARCHAR(32) NULL,
    # game_popularity INT NULL,
    # game_id INT,
    # game_giantbomb_id INT NULL,
    # game_box_large VARCHAR(90) NULL,
    # game_box_template VARCHAR(99) NULL,
    # game_logo_large VARCHAR(91) NULL,
    # game_localized_name VARCHAR(32) NULL,
    # game_locale VARCHAR(5) NULL,
    # PRIMARY KEY (game_id)
    query = """
    INSERT INTO game (game_name, game_popularity, game_id,game_giantbomb_id,game_box_large,game_box_template,game_logo_large,game_localized_name,game_locale) 
    VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s);
    """

    with connection.cursor() as cursor:
        print('Executando query:')
        cursor.execute(
            query, (obj['name'], obj['popularity'], obj['_id'], obj['giantbomb_id'], obj['box']['large'], obj['box']['template'], obj['logo']['large'], obj['localized_name'], obj['locale']))
        cursor.execute('COMMIT')
