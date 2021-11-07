from datetime import datetime


class Tournament:
    def __init__(self, name, location, time_control,
                 description):
        self.name = name
        self.location = location
        self.start_date = datetime.today().strftime('%d-%m-%Y')
        self.end_date = datetime.today().strftime('%d-%m-%Y')
        self.turns = 4
        self.rounds_list = []
        self.players_list: []
        self.time_control = time_control
        self.description = description
