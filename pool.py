# The plan for this branch is to in fast time eliminate players from the player pool if they are guaranteed to not be in
# the optimal lineup.  
#
# Idea 1: FInd all players with same or cheaper salary and a higher projection. (complexity n).
#   Add those players to the lineup until there is no space for the player in question (more players makes it likely to
#       end early so it shouldn't practically making it more complex.)
#   Do it for every player (complexity n**2 total)
#   We might be able to speed this up because if a player who has been eliminated AND same position is "better" then we know right away
#   the player is eliminated.
#   
# Idea 2: Start with the highest projected player.  If every player cheaper than the player we have added can be added
# to the lineup then the player is not in. After a player is eliminated eliminate any player at the same position
# "worse" than that player.

import pandas as pd

from player import Player
import constants


class Pool:
    """only supports dk atm"""

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)[['NAME','TEAM','OPPONENT','POSITION','SALARY','SITE_ID','PTS','RBS','ASTS','STLS','BLKS','TOS','THREES','DOUBLE_DOUBLE','TRIPLE_DOUBLE']]
        self.pool = constants.dk_pool_default_dic
        self.current_index = 0
        self.current_position = 0
        self.positional_index = 0

        for index, row in self.df.iterrows():
            stat_projections={}
            stat_projections[constants.pts] = row['PTS']
            stat_projections[constants.rbs] = row['RBS']
            stat_projections[constants.asts] = row['ASTS']
            stat_projections[constants.stls] = row['STLS']
            stat_projections[constants.blks] = row['BLKS']
            stat_projections[constants.tos] = row['TOS']
            stat_projections[constants.threes] = row['THREES']
            stat_projections[constants.dd] = row['DOUBLE_DOUBLE']
            stat_projections[constants.td] = row['TRIPLE_DOUBLE']
            
            new_player = Player(name=row['NAME'],team=row['TEAM'],opp=row['OPPONENT'],position=row['POSITION'],salary=row['SALARY'],dfs_site_id=row['SITE_ID'],stat_projections=stat_projections,site_name=constants.dk

            self.pool[new_player.position].append(new_player)

    def __repr__(self):
        return repr(self.df)
    
    def __len__(self):
        return sum(len(self.pool[position]) for position in self.pool.keys())

    def __getitem__(self, arg):
        #this could be changed to binary search
        if arg < 0 or arg >= self.__len__():
            raise IndexError
        for position in constants.dk_pool_order:
            if arg > len(self.pool[position]) - 1:
                arg -= len(self.pool[position])
            else:
                return self.pool[position][arg]

    def parse_pool(self):
        pass
    
    def current_player(self):
        try:
            return self.pool[constants.dk_pool_order[self.current_position]][self.positional_index]
        except:
            raise IndexError

    def next_player(self):
        if len(self.pool[constants.dk_pool_order[self.current_position]]) > self.positional_index + 1:
            self.positional_index += 1
            self.current_index += 1
        else:
            self.positional_index = 0
            self.current_index += 1
            self.current_position += 1
        
        while len(self.pool[constants.dk_pool_order[self.current_position]]) == 0:
            self.current_position += 1
            
