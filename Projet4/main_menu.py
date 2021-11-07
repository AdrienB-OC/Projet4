from models import*
from sqlitetest import*


menu_options = {
    1: "Ajouter un joueur",
    2: "Afficher la liste des joueurs",
    3: "Mettre à jour le classement des joueurs",
    4: "Nouveau Tournoi",
    5: "Afficher la liste des tournois",
    6: "Fermer le programme"
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    create_player()


def option2():
    player_list = fetch_all_data()
    player_list = sorted(player_list, key=lambda x: x.ranking, reverse=False)
    for player in player_list:
        print("ID: ", player.t_id)
        print("Nom: ", player.name)
        print("Prénom: ", player.surname)
        print("Date de Naissance: ", player.birth_date)
        print("Sexe: ", player.gender)
        print("Classement: ", player.ranking)
        print("")


def option3():
    update_all_ranking()


def option4():
    player_list = create_player_list()
    create_tournament(player_list)


def option5():
    print("En cours d'implémentation")


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except option < 0 or option > 6 or option is not int:
            print('Wrong input. Please enter a number ...')

        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            print('Fermeture du programme')
            exit()
        else:
            print('Erreur. Entrez un nombre entre 1 et 6')
