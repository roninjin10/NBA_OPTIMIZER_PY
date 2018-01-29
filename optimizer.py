import copy
import constants
from dfs_site import DFS_Site
from lineup import Lineup
from player import Player
from pool import Pool

class __Optimizer:

    def __init__(self, pool=None, site=constants.dk, lineups=[]):
        self.site = Site(site)
        self.pool = pool
        self.lineups = lineups
        self.memoized = {}

        if self.pool == None:
            pool = Pool()

    def __len__(self):
        return len(lineups)

    def __repr__(self):
        return repr(lineups)

    def __getitem__(self, key):
        return lineups[key]


class Dynamic_Optimizer(__Optimizer):

    def __recursive_step(self, pool, lu):
        self.recursion_counter += 1
        print(self.recursion_counter)

        if len(lu) == len(self.site.roster_construction)
            return lu

        if pool.current_index == len(pool):
            return None

        lu_key = lu.dic_key(pool.current_position, pool.positional_index)
        if lu_key in self.memoized.keys():
            return lu.merge_lineups(self.memoized[lu_key])

        lu_take = copy.deepcopy(lu)
        take_player = pool.current_player()
        pool.next_player()
        if lu_take.add_player(take_player) == 0:
            lu_take = self.__recursive_step(pool,lu_take)
        else:
            lu_take = None

        lu_pass = copy.deepcopy(lu)
        lu_pass = self.__recursive_step(pool,lu_pass)

        if lu_pass == None or lu_take == None:
            return lu_take if lu_pass == None else lu_take
        else:
            return lu_take if lu_take.dfs_projection() >= lu_pass else lu_pass
        


    def optimize(self, n=1):
        self.recursion_counter = 0
        
        lu = Lineup(site_name=constants.dk)
        pool = self.pool
        
        opt = Optimizer(pool, lu)


class Genetic_Optimizer(__Optimizer):

    def optimize(self, n):
        pass

