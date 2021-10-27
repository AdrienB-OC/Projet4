import json
from views import View
from player_class import*
from pairing import*
from sqlitetest import add_player_data


def create_player():
    data = View.player_input()
    player = Player(data.name, data.surname,
                    data.birth_date, data.gender, data.ranking)
    add_player_data(player)
    return player


def create_tournament_player():
    data = View.player_input()
    player = Tournament_Player(data.ranking, data.name, data.surname,
                               data.birth_date, data.gender)
    return player


def create_match(player_1, player_2):
    winner = View.match_input(View, player_1, player_2)
    match_id = []
    if int(player_1.t_id) < int(player_2.t_id):
        match_id += [str(int(player_1.t_id)) + str(int(player_2.t_id))]
    else:
        match_id += [str(int(player_2.t_id)) + str(int(player_1.t_id))]
    if winner == '1':
        player_1.points += 1
        print(player_1.surname + ' ' + player_1.name + ' gagne !')
        return 'win', 'lose', match_id
    elif winner == '2':
        player_2.points += 1
        print(player_2.surname + ' ' + player_2.name + ' gagne !')
        return 'lose', 'win', match_id
    elif winner == '3':
        player_1.points += 0.5
        player_2.points += 0.5
        print('Match Nul !')
        return 'draw', 'draw', match_id


def create_round(player_list_top, player_list_bottom, match_id):
    match_1 = create_match(player_list_top[0], player_list_bottom[0])
    match_id1 = match_1[2]

    match_2 = create_match(player_list_top[1], player_list_bottom[1])
    match_id2 = match_2[2]

    match_3 = create_match(player_list_top[2], player_list_bottom[2])
    match_id3 = match_3[2]

    match_4 = create_match(player_list_top[3], player_list_bottom[3])
    match_id4 = match_4[2]

    results = [(player_list_top[0].name, match_1[0]),
               (player_list_bottom[0].name, match_1[1])] + \
        [(player_list_top[1].name, match_2[0]),
            (player_list_bottom[1].name, match_2[1])] + \
        [(player_list_top[2].name, match_3[0]),
            (player_list_bottom[2].name, match_3[1])] + \
        [(player_list_top[3].name, match_4[0]),
            (player_list_bottom[3].name, match_4[1])]

    match_id += match_id1 + match_id2 + match_id3 + match_id4

    return results, match_id


def create_tournament(player_list):
    match_id = []
    tournament = View.tournament_input()
    turns = int(tournament.turns)

    for i in range(0, turns):
        print('Round ' + str(i+1))
        if i == 0:
            pairs = pairing_r1(player_list)
            player_list_top = pairs[0]
            player_list_bottom = pairs[1]
            for j in range(0, 4):
                print(player_list_top[j].name + ' ' +
                      player_list_top[j].surname +
                      ' vs ' +
                      player_list_bottom[j].name + ' ' +
                      player_list_bottom[j].surname)
            r_result = create_round(player_list_top, player_list_bottom,
                                    match_id)
            r1_result = r_result[0]
            print(''.join(map(str, r1_result)))
        elif i > 0:
            pairs = pairing(player_list_top, player_list_bottom, match_id)
            player_list_top = pairs[0]
            player_list_bottom = pairs[1]
            for j in range(0, 4):
                print(player_list_top[j].name + ' ' +
                      player_list_top[j].surname +
                      ' vs ' +
                      player_list_bottom[j].name + ' ' +
                      player_list_bottom[j].surname)
            r_result = create_round(player_list_top, player_list_bottom,
                                    match_id)
            if i == 1:
                r2_result = r_result[0]
            elif i == 2:
                r3_result = r_result[0]
            elif i == 3:
                r4_result = r_result[0]
            print(''.join(map(str, r_result)))
    print('Tournoi terminé')
    return r1_result, r2_result, r3_result, r4_result




