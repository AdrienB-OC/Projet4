class Tournament:
    def __init__(self, name, location, start_date, end_date, time_control,
                 description):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.turns = 4
        self.rounds_list = []
        self.players_list: []
        self.time_control = time_control
        self.description = description
