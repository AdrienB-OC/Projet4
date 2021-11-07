from player_class import Player
from tournament_class import Tournament


class View:
    def player_input():
        name = input("Nom du joueur : ")
        surname = input("Prénom du joueur : ")
        birth_date = input("Date de Naissance (JJ/MM/AAAA) : ")
        gender = input("Sexe (M/F) : ")
        ranking = input("Classement : ")
        player = Player(name, surname, birth_date, gender, ranking)
        return player

    def match_input(self, player1, player2):
        print('1 - ' + player1.name + ' ' + player1.surname + '\n'
              '2 - ' + player2.name + ' ' + player2.surname + '\n'
              '3 - Match nul \n')
        winner = input('Entrez le chiffre correspondant au gagnant du match :')
        return winner

    def tournament_input():
        name = input('Nom du tournoi : ')
        location = input('Lieu où se déroule le tournoi : ')
        time_control = input('Contrôle du temps : ')
        description = input('Description : ')

        tournament = Tournament(name, location, time_control, description)
        return tournament



