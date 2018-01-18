import pandas as pd
import numpy as np 


#constants
dk = 'DRAFTKINGS'
fd = 'FANDUEL'


#classes
class Site:

	def __init_(self, name = dk)
		self.name = name

	def roster_construction(self):
		if self.name == dk:
			return (
				('PG'),
				('SG'),
				('SF'),
				('PF'),
				('C'),
				('PG','SG'),
				('SF','PF'),
				('PG','SG','SF','PF','C'),
				)

	def salary_cap(self):
		if self.name == dk:
			return 50000

	def value(self,projection,salary):
		if name == dk:
			min_proj, value_mult, min_sal = 18, 4.2, 3000

		return projection - (min_proj + value_mult * (salary - min_sal)/1000)

class Player:

    def __init__(self, name=None, team=None, opp=None, position=(None, None), projection=None, salary=None, real_value = None, site_id = None):
        self.player_info = {}
        self.player_info['name'] = name
        self.player_info['team'] = team
        self.player_info['opp'] = opp
        self.player_info['position'] = position
        self.player_info['projection'] = projection
        self.player_info['salary'] = salary
        self.player_info['real_value'] = real_value
        self.player_info['site_id'] = site_id

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


class Lineup:

    def __init__(self, site = dk):

        lineup_site = Site(site)
        
        self.roster = {}
        for i in range(len(Site.roster_construction)):
        	self.roster[i] = None

        self.salary_cap = Site.salary_cap

    def salary(self):
        return sum(plr.salary for plr in self.roster.items() if not plr is None)

    def points(self):
        return sum(plr.projection for plr in self.roster.items() if not plr is None)

    def create_key(self, current_position, current_player_num):
        return "Pos: " + current_position + " PlNum: " + current_player_num + " Sal: " + str(self.salary()) + " Positions: " + ''.join(str(pos != None) for pos in self.roster.items())


    def merge_lineup(self, lineup):
        for pos in self.roster.keys():
        	if self[pos] = None:
        		self[pos] = lineup[pos]

    def erase_lineup(self):
        for pos in self.roster.keys():
        	self[pos] = None

    def add_player(self, new_player, roster_spot=None):
        #adds a player to a lineup to a specified roster_spot. Overwrites player if roster_spot specified
        # If roster_spot is not given, it puts the player in the valid, empty roster spot that provides most future roster flexibility
        # method returns a boolean based on if the player was added or not
        if roster_spot != None:
            self.roster[roster_spot] = new_player


    def is_valid_salary(self):
        return self.salary() <= self.salary_cap

    def is_valid_team(self):
        team_opponent = []
        for plr in self.roster.items():
            if team_opponent == []:
                team_opponent.append(plr.get_info('team'))
                team_opponent.append(plr.get_info('opp'))
            else:
                if not plr.get_info('team') in team_opponent:
                    return True
        return False

    def is_valid_positional(self):
        #returns boolean based on if the lineup has every position filled
        for plr in self.roster.items():
            if plr is None:
                return False
        return True

    def is_valid(self):
        return self.is_valid_positional() and self.is_valid_salary() and self.is_valid_team()

    def copy_lineup(self):
        #returns a copy of the same lineup
        out = Lineup()
        out.roster = self.roster
		return out


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

if __name__ == "__main__":
	player_pool = Pool()

	memoized = {}
