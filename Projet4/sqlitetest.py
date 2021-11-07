import sqlite3
from player_class import Tournament_Player


def fetch_all_data():
    try:
        sqlite_connection = sqlite3.connect('players_data.db')
        cur = sqlite_connection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from players_data"""
        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        print("Liste des joueurs")
        print("ID | NOM | Prénom | Classement ")
        player_list = []
        for row in records:
            player = Tournament_Player(row[0], row[1], row[2], row[3], row[4],
                                       row[5])
            player_list.append(player)

        cur.close()
        return player_list

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def fetch_player_data(player_id):
    try:
        sqlite_connection = sqlite3.connect('players_data.db')
        cur = sqlite_connection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from players_data"""
        cur.execute(sqlite_select_query)
        records = cur.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Surname: ", row[2])
            print("Birth Date: ", row[3])
            print("Gender: ", row[4])
            print("Ranking: ", row[5])
            print("\n")

        cur.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed")


def update_player_ranking(player_id, new_rank):
    try:
        sqlite_connection = sqlite3.connect('players_data.db')
        cur = sqlite_connection.cursor()

        sqlite_update_query = """UPDATE players_data set ranking = ? 
                                 where id = ?"""
        data = (new_rank, player_id)
        cur.execute(sqlite_update_query, data)
        sqlite_connection.commit()
        cur.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()


def update_all_ranking():
    player_list = fetch_all_data()
    for player in player_list:
        print(player.name, player.surname)
        print('Classement : ', player.ranking)
        new_rank = input('Entrez le nouveau classement de ce joueur : ')
        update_player_ranking(player.t_id, new_rank)
        print('Classement mis à jour avec succès !')


def add_player_data(player):
    try:
        sqlite_connection = sqlite3.connect('players_data.db')
        cur = sqlite_connection.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS players_data (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                surname TEXT NOT NULL,
                                birth_date NOT NULL,
                                gender TEXT NOT NULL,
                                ranking INTEGER NOT NULL);""")
        print("Successfully Connected to SQLite")

        cur.execute("""INSERT INTO players_data
                   (name, surname, birth_date, gender, ranking)
                   VALUES (?, ?, ?, ?, ?)""", (player.name,
                                               player.surname,
                                               player.birth_date,
                                               player.gender,
                                               player.ranking))
        sqlite_connection.commit()
        print("Record inserted successfully into players_data table ",
              cur.rowcount)
    except sqlite3.Error as error:
        print('Erreur lors de la création de données', error)
    finally:
        if sqlite_connection:
            cur.close()


def save_tournament_data(round1, round2, round3, round4, tournament,
                         players_list):
    try:
        sqlite_connection = sqlite3.connect('players_data.db')
        cur = sqlite_connection.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS tournament_data (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        location TEXT NOT NULL,
                                        start_date TEXT NOT NULL,
                                        end_date TEXT NOT NULL,
                                        round1 TEXT NOT NULL,
                                        round2 TEXT NOT NULL,
                                        round3 TEXT NOT NULL,
                                        round4 TEXT NOT NULL,
                                        players_id TEXT NOT NULL);""")
        print("Successfully Connected to SQLite")
        players_id = []
        for i in range(0, 8):
            players_id.append(players_list[i].t_id)

        cur.execute("""INSERT INTO players_data
                           (name, location, start_date, end_date,
                           round1, round2, round3, round4, players_id)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (tournament.name,
                     tournament.location,
                     tournament.start_date,
                     tournament.end_date,
                     round1,
                     round2,
                     round3,
                     round4,
                     players_id))
        sqlite_connection.commit()
        print("Record inserted successfully into tournament_data table ",
              cur.rowcount)

    except sqlite3.Error as error:
        print("Erreur lors de l'écriture des données", error)
    finally:
        if sqlite_connection:
            cur.close()
