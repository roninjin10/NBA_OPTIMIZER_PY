#this was never touched

class Pool:

    def __init__(self):
        __pool = []
        __orig_pool = pd.DataFrame({})

    def __init_pool(self):
    	for index, row in __orig_pool.interrows():
			new_player = Player(name=row['Name'], team=row['Team'], opp=None, position=(None, None), projection=None, salary=None, real_value = None, site_id = None)

    def create_pool_from_csv(self, csv):
        __orig_pool = pd.read_csv('./projections.csv')[['Name','Projection','Salary','Position','Team']]
        __init_pool(self)

    def create_positional_list(self, pos):
        #creates a list of players eligible for a specific position. PG, SG, SF, PF, C, G, F, Flex
        out = {}
        if pos == 'f':
            return [player for player in self.__pool if 'sf' in player.get_info('position') or 'pf' in player.get_info('position')]
        elif pos == 'g':
            return [player for player in self.__pool if 'pg' in player.get_info('position') or 'sg' in player.get_info('position')]
        else:
            return [player for player in self.__pool if pos in player.get_info('position')]

    def remove_player(self, player_name='', index=-1):
        #removes player from a list
        if index != -1:
            removed_player =__pool.pop(index)
        elif player_name != '':
            removed_player = __pool.pop(__pool.index(player_name))

    def pop_player(self, player_name='', index=-1):
        #removes player from a list and returns that player
        if index != -1:
            return __pool.pop(index)
        elif player_name != '':
            return __pool.pop(__pool.index(player_name))

    def add_player(self, player_name):
        #adds a player to the player_pool not necessary atm
        pass

    def restore_player_pool(self):
        self.__pool = self.__orig_pool

    def get_player_index(self, current_position, current_player_num):
        pass
        #gets the player index in __pool based on current position and player_num at position
