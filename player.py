class Player:

    def __init__(self, info = {}):
        self.name = info[name]
        self.team = info[team]
        self.opp = info[opp]
        self.position = info[position]
        self.salary = info[salary]
        self.real_value = info[real_value]
        self.site_id = info[site_id]

        self.projection = {}
        for category in stat_categories:
            self.projection[category] = info[category] 

    def copy_player(self):
        #returns an identical player
        new_player = Player
        new_player.player_info = self.player_info
        return new_player

    def change_player_info(self, info_dic):
        #info_dic is a dictionary containing some player_info
        for info in info_dic.keys:
            self.player_info[info] = info_dic[info]

    def get_info(self, info_to_get):
        return self.player_info[info_to_get]

    def set_info(self, info_to_set, info_value):
		self.player_info[info_to_set] = info_value

