import datetime


class Round:
    def __init__(self, round_number):
        self.start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = ''
        self.round_number = round_number
        self.match_list = []
