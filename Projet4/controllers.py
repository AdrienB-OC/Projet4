from models import*


player1 = Tournament_Player('nom', 'prenom', '01/01/2001', 'M', '8', 1)
player2 = Tournament_Player('nom2', 'prenom2', '01/01/2001', 'F', '5', 2)
player3 = Tournament_Player('nom3', 'prenom3', '01/01/2001', 'M', '6', 3)
player4 = Tournament_Player('nom4', 'prenom4', '01/01/2001', 'F', '7', 4)
player5 = Tournament_Player('nom5', 'prenom5', '01/01/2001', 'M', '1', 5)
player6 = Tournament_Player('nom6', 'prenom6', '01/01/2001', 'F', '2', 6)
player7 = Tournament_Player('nom7', 'prenom7', '01/01/2001', 'M', '3', 7)
player8 = Tournament_Player('nom8', 'prenom8', '01/01/2001', 'F', '4', 8)

player_list = [player1] + [player2] + [player3] + [player4] + [player5] + \
              [player6] + [player7] + [player8]

tournament = create_tournament(player_list)

