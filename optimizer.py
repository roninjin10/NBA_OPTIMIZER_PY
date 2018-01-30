import copy
import constants
from dfs_site import DFS_Site
from lineup import Lineup
from player import Player
from pool import Pool
import logging

def main():
    opt = Dynamic_Optimizer('./small_projections.csv')
    lu = opt.optimize()
    print(opt)

class __Optimizer:

    def __init__(self, pool_path, dfs_site=constants.dk, lineups=[]):
        self.dfs_site = DFS_Site(dfs_site)
        self.pool = Pool(pool_path)
        self.lineups = lineups
        self.memoized = {}

        self.start_logging()

    def __len__(self):
        return len(lineups)

    def __repr__(self):
        return repr(self.lineups)

    def __getitem__(self, key):
        return lineups[key]

    def start_logging(self, level=logging.DEBUG):
        logging.basicConfig(filename='logfile.log',level=level)


class Dynamic_Optimizer(__Optimizer):

    def __recursive_step(self, pool, lu):
        self.recursion_counter += 1
        counter = 'recursion ' + str(self.recursion_counter)

        logging.debug('{} Current Lineup/n {}'.format(counter, repr(lu)))
        logging.debug('{} pool.current_index == {}'.format(counter,repr(pool.current_index)))
        logging.debug('{} pool.current_position == {}'.format(counter,repr(pool.current_position)))
        logging.debug('{} pool.positional_index == {}'.format(counter,repr(pool.positional_index)))
 
        
        if len(lu) == len(self.dfs_site.roster_construction):
            logging.debug('{} Lineup complete returning lineup/n {}'.format(counter,repr(lu)))
            
            return lu

        if pool.current_index == len(pool) - 1:
            logging.debug('{} no players left in pool returning none. len(lu) == {} pool.current_index == {}'.format(counter, str(len(lu)), str(pool.current_index)))
            
            return None

        lu_key = lu.dic_key(pool.current_position, pool.positional_index)
        
        logging.debug('{} lu_key == {}'.format(counter,lu_key))

        if lu_key in self.memoized.keys():
            logging.debug('{} lu_key in self.memoized.keys merging lu with memoized lu /n {} /n {}'.format(counter,repr(lu),repr(self.memoized[lu_key])))
            
            return lu.merge_lineups(self.memoized[lu_key])

        lu_take = copy.deepcopy(lu)
        
        take_player = pool.current_player()
        
        logging.debug('{} Starting take_player on player {}/n{}'.format(counter,str(pool.current_index),repr(take_player)))
        
        pool.next_player()

        logging.debug('{} pool.next_player() now pool.current_index == {}'.format(counter,str(pool.current_index)))

        if lu_take.add_player(take_player) == 0:
            logging.debug('{} lu_take.add_player was succesful'.format(counter))

            lu_take = self.__recursive_step(pool,lu_take)

            logging.debug('{} lu_take finished and returned/n{}'.format(counter,repr(lu_take)))
        else:
            logging.debug('{} lu_take.add_player was unsuccesful with code {}'.format(counter,str(lu_take.add_player(take_player))))
            lu_take = None

        logging.debug('{} starting lu_pass'.format(counter))

        lu_pass = copy.deepcopy(lu)
        lu_pass = self.__recursive_step(pool,lu_pass)

        if lu_pass == None or lu_take == None:
            if lu_pass == None and lu_take == None:
                logging.debug('{} both lineups failed returning none'.format(counter))
            else:
                logging.debug('{} {} failed returning the other'.format(counter,'lu_pass' if lu_pass == None else 'lu_take'))

            return lu_take if lu_pass == None else lu_take
        else:
            logging.debug('{} comparing projections lu_take {} and lu_pass {}'.format(counter,str(lu_take.dfs_projection()),str(lu_pass.dfs_projection())))

            return lu_take if lu_take.dfs_projection() >= lu_pass else lu_pass
        


    def optimize(self, n=1):
        logging.debug('start optimizer n = {}'.format(n))
        
        self.recursion_counter = 0
        
        lu = Lineup(site_name=constants.dk)
        pool = self.pool
        
        logging.debug('Pool /n' + repr(pool))

        opt = self.__recursive_step(pool, lu)

        return opt


class Genetic_Optimizer(__Optimizer):

    def optimize(self, n):
        pass


if __name__ == '__main__':
    main()
