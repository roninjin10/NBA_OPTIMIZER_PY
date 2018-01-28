#this was never touched
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
            
            new_player = Player(name=row['NAME'],team=row['TEAM'],opp=row['OPPONENT'],position=row['POSITION'],salary=row['SALARY'],dfs_site_id=row['SITE_ID'],stat_projections=stat_projections,site_name=constants.dk)
            #print(new_player)

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
            
