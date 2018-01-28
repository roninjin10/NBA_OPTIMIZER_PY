import constants
from dfs_site import DFS_Site
from lineup import Lineup
from player import Player
from pool import Pool

import unittest

import copy


empty_lineup = Lineup()

test_stat_projections = {constants.pts : 10, constants.rbs: 1, constants.asts: 1, constants.stls: 1, constants.blks: 1, constants.tos: 1, constants.threes: 1, constants.dd: 0, constants.td: 0}  

test_player = Player(name='Kyle Anderson', team='SA', opp='CLE', position='PG/SF', salary=3000, dfs_site_id ='152333', stat_projections=test_stat_projections, site_name=constants.dk)

pg1_stats = {constants.pts : 20, constants.rbs: 3, constants.asts: 9, constants.stls: 2, constants.blks: .2, constants.tos: 1.8, constants.threes: 2, constants.dd: .3, constants.td: .2} #42.8 dkpoints 
pg2_stats = {constants.pts : 13, constants.rbs: 2, constants.asts: 4.5, constants.stls: .8, constants.blks: .2, constants.tos: 1.5, constants.threes: 1, constants.dd: 0, constants.td: 0}  
sg1_stats = {constants.pts : 27, constants.rbs: 1.4, constants.asts: 2.5, constants.stls: .2, constants.blks: .1, constants.tos: 2, constants.threes: 3.2, constants.dd: 0, constants.td: 0}  #33.7 dkpoints
sg2_stats = {constants.pts : 9, constants.rbs: 2.5, constants.asts: 1.5, constants.stls: 1.2, constants.blks: 1.1, constants.tos: 1, constants.threes: 1.3, constants.dd: 0, constants.td: 0}  
sf1_stats = {constants.pts : 10, constants.rbs: 1, constants.asts: 1, constants.stls: 1, constants.blks: 1, constants.tos: 1, constants.threes: 1, constants.dd: 0, constants.td: 0}  
sf2_stats = {constants.pts : 10, constants.rbs: 1, constants.asts: 1, constants.stls: 1, constants.blks: 1, constants.tos: 1, constants.threes: 1, constants.dd: 0, constants.td: 0}  
pf1_stats = {constants.pts : 20, constants.rbs: 10, constants.asts: 1, constants.stls: 1, constants.blks: 2.5, constants.tos: 1, constants.threes: 2, constants.dd: .8, constants.td: 0}  
pf2_stats = {constants.pts : 10, constants.rbs: 1, constants.asts: 1, constants.stls: 1, constants.blks: 1, constants.tos: 1, constants.threes: 1, constants.dd: 0, constants.td: 0}  
c1_stats = {constants.pts : 10, constants.rbs: 1, constants.asts: 1, constants.stls: 1, constants.blks: 1, constants.tos: 1, constants.threes: 1, constants.dd: 0, constants.td: 0}  
c2_stats = {constants.pts : 10, constants.rbs: 1, constants.asts: 1, constants.stls: 1, constants.blks: 1, constants.tos: 1, constants.threes: 1, constants.dd: 0, constants.td: 0}  


pg1 = Player(name='Chris Paul', team='HOU', opp='NY', position='PG', salary=9000, dfs_site_id ='152334', stat_projections=pg1_stats, site_name=constants.dk)
pg2 = Player(name='George Hill', team='SAC', opp='PHO', position='PG/SG', salary=5000, dfs_site_id ='152335', stat_projections=pg2_stats, site_name=constants.dk)
sg1 = Player(name='Devin Booker', team='PHO', opp='SAC', position='SG', salary=8000, dfs_site_id ='152336', stat_projections=sg1_stats, site_name=constants.dk)
sg2 = Player(name='Danny Green', team='SA', opp='CLE', position='SG/SF', salary=4000, dfs_site_id ='152337', stat_projections=sg2_stats, site_name=constants.dk)
sf1 = Player(name='Trevor Ariza', team='HOU', opp='NY', position='SF', salary=5000, dfs_site_id ='152338', stat_projections=sf1_stats, site_name=constants.dk)
sf2 = Player(name='Jeff Green', team='CLE', opp='SA', position='SF/PF', salary=3800, dfs_site_id ='152339', stat_projections=sf2_stats, site_name=constants.dk)
pf1 = Player(name='Kevin Love', team='CLE', opp='SA', position='PF/C', salary=7500, dfs_site_id ='152340', stat_projections=pf1_stats, site_name=constants.dk)
pf2 = Player(name='Kristaps Porzingis', team='NY', opp='HOU', position='PF', salary=8800, dfs_site_id ='152341', stat_projections=pf2_stats, site_name=constants.dk)
c1 = Player(name='Alex Len', team='PHO', opp='SAC', position='C', salary=4100, dfs_site_id ='152342', stat_projections=c1_stats, site_name=constants.dk)
c2 = Player(name='Pau Gasol', team='SA', opp='CLE', position='C', salary=5400, dfs_site_id ='152343', stat_projections=c2_stats, site_name=constants.dk)

test_players = [test_player, pg1, pg2, sg1, sg2, sf1, sf2, pf1, pf2, c1, c2]

class Test_Pool(unittest.TestCase):
    
    def test_init(self):
        pool = Pool('./small_projections.csv')
        
        self.assertEqual(len(pool.pool['PG']),5)
        self.assertEqual(len(pool.pool['PG/SG']),3)
        self.assertEqual(len(pool.pool['SG']),1)
        self.assertEqual(len(pool.pool['SG/SF']),4)
        self.assertEqual(len(pool.pool['SF']),0)
        self.assertEqual(len(pool.pool['SF/PF']),2)
        self.assertEqual(len(pool.pool['PF']),0)
        self.assertEqual(len(pool.pool['PF/C']),4)
        self.assertEqual(len(pool.pool['C']),4)
        self.assertEqual(len(pool.pool['PG/SF']),1)

    def test_repr(self):
        pool = Pool('./small_projections.csv')
        
        self.assertEqual(repr(pool),
            pd.read_csv('./small_projections.csv')[['NAME','TEAM','OPP','POSITION','SALARY','SITE_ID','PTS','RBS','ASTS','STLS','BLKS','TOS','THREES','DOUBLE_DOUBLE','TRIPLE_DOUBLE']])
    
    def test_len(self):
        pool = Pool('./small_projections.csv')
        self.assertEqual(len(pool),24)

    def test_get_item(self):
        pool = Pool('./small_projections.csv')
        self.assertEqual(pool[5].name,'Avery Bradley')
        self.assertEqual(pool[0].name,'John Wall')
        self.assertEqual(pool[23].name,'Denzel Valentine')

    def test_next_player_and_current_player(self):
        #these tests could be seperated by testing each using the player indexes instead of via using each other
        pool = Pool('./small_projections.csv')
        
        self.assertEqual(pool.current_player().name, 'John Wall')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Tony Parker')

        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Goran Dragic')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Ricky Rubio')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Dennis Schroder')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Avery Bradley')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Shabazz Napier')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Tyler Johnson')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Gary Harris')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'DeMar DeRozan')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Khris Middleton')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Marcus Smart')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Dion Waiters')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Michael Beasley')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'T.J. Warren')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Kelly Olynyk')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Al Horford')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Taj Gibson')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Bobby Portis')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Karl-Anthony Towns')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Nikola Jokic')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Brook Lopez')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Rudy Gobert')
        
        pool.next_player()
        self.assertEqual(pool.current_player().name, 'Denzel Valentine')
        
        with self.assertRaises(IndexError):
            pool.next_player()

class Test_Player(unittest.TestCase):

    def setUp(self):
        self.test_player = copy.deepcopy(test_player)       
    
    def test_repr(self):
        representation = self.test_player.__repr__
        #print(self.test_player)
 
    def test_dfs_projection(self):
        self.assertEqual(self.test_player.dfs_projection, 16.75)

    def test_value(self):
        self.assertEqual(self.test_player.dfs_value, -1.25)

    def test_change_site(self):
        pass

    def test_change_stat_projection(self):
        new_stats = {constants.pts: 1, constants.rbs: 0, constants.asts: 1, constants.stls: 2, constants.blks: 0, constants.tos: 2, constants.threes: 0, constants.dd: 1, constants.td: 1 }
        
        self.test_player.change_stat_projections(new_stats)
        
        for category in self.test_player.stat_projections.keys():
            self.assertEqual(new_stats[category], self.test_player.stat_projections[category])
        
        self.assertEqual(self.test_player.dfs_projection, 10)
        self.assertEqual(self.test_player.dfs_value , -8)
   
    def test_dk_positions(self):
        self.assertEqual(len(test_player.dk_positions()),2)
        self.assertEqual(test_player.dk_positions()[0],'PG')
        self.assertEqual(test_player.dk_positions()[1],'SF')
        
        self.assertEqual(len(c1.dk_positions()),1)
        self.assertEqual(c1.dk_positions()[0],'C')

    def test_full_site_id(self):
        self.assertEqual(self.test_player.full_site_id(), 'Kyle Anderson (152333)')


class Test_Lineup(unittest.TestCase):

    def setUp(self):
        self.lineup = copy.deepcopy(empty_lineup)
        
    def test_salary(self):
        self.lineup = copy.deepcopy(empty_lineup) 
        self.assertEqual(self.lineup.salary(), 0)

        self.lineup.roster[constants.pg] = pg1
        self.assertEqual(self.lineup.salary(),9000)

        self.lineup.roster[constants.sg] = sg1
        self.assertEqual(self.lineup.salary(), 17000) 

    def test_dfs_projection(self):
        self.lineup = copy.deepcopy(empty_lineup)
        self.assertEqual(self.lineup.dfs_projection(), 0)

        self.lineup.roster[constants.pg] = pg1
        self.assertEqual(self.lineup.dfs_projection(), 42.8)
        
        self.lineup.roster[constants.sg] = sg1
        self.assertEqual(self.lineup.dfs_projection(), 76.5)

    def test_dic_key(self):
        """could use more tests but I'm confident this will work if the other methods work"""
        self.lineup = copy.deepcopy(empty_lineup)
        self.lineup.roster[constants.pg] = pg1
        key1 = self.lineup.dic_key(1,5)
        self.lineup.roster[constants.sg] = sg1
        key2 = self.lineup.dic_key(1,5)

        self.assertEqual(key1 == key2, False)
  
    def test_merge_lineup(self):
        lineup_to_merge = copy.deepcopy(empty_lineup)
        self.lineup.roster[constants.pg] = pg1
        self.lineup.roster[constants.sg] = sg1
        self.lineup.roster[constants.sf] = sf1
        self.lineup.roster[constants.pf] = pf1
        self.lineup.roster[constants.c] = c1
        self.lineup.roster[constants.g] = pg2
        self.lineup.roster[constants.f] = sf2
        self.lineup.roster[constants.flex] = c2

        self.lineup.merge_lineups(lineup_to_merge)
        
        self.assertEqual(self.lineup.roster[constants.pg],pg1)
        self.assertEqual(self.lineup.roster[constants.sg] , sg1)
        self.assertEqual(self.lineup.roster[constants.sf] , sf1)
        self.assertEqual(self.lineup.roster[constants.pf] , pf1)
        self.assertEqual(self.lineup.roster[constants.c] , c1)
        self.assertEqual(self.lineup.roster[constants.g] , pg2)
        self.assertEqual(self.lineup.roster[constants.f] , sf2)
        self.assertEqual(self.lineup.roster[constants.flex] , c2)

        lineup_to_merge.roster[constants.pg] = pg2
        lineup_to_merge.roster[constants.sg] = sg2
        lineup_to_merge.roster[constants.sf] = sf2
        lineup_to_merge.roster[constants.pf] = pf2
        lineup_to_merge.roster[constants.c] = c2
        lineup_to_merge.roster[constants.g] = pg1
        lineup_to_merge.roster[constants.f] = sf1
        lineup_to_merge.roster[constants.flex] = c1

        self.lineup.merge_lineups(lineup_to_merge)
        
        self.assertEqual(self.lineup.roster[constants.pg],pg1)
        self.assertEqual(self.lineup.roster[constants.sg] , sg1)
        self.assertEqual(self.lineup.roster[constants.sf] , sf1)
        self.assertEqual(self.lineup.roster[constants.pf] , pf1)
        self.assertEqual(self.lineup.roster[constants.c] , c1)
        self.assertEqual(self.lineup.roster[constants.g] , pg2)
        self.assertEqual(self.lineup.roster[constants.f] , sf2)
        self.assertEqual(self.lineup.roster[constants.flex] , c2)
 
        self.lineup.roster[constants.flex] = None
        self.lineup.roster[constants.c] = None

        self.lineup.merge_lineups(lineup_to_merge)

        self.assertEqual(self.lineup.roster[constants.pg],pg1)
        self.assertEqual(self.lineup.roster[constants.sg] , sg1)
        self.assertEqual(self.lineup.roster[constants.sf] , sf1)
        self.assertEqual(self.lineup.roster[constants.pf] , pf1)
        self.assertEqual(self.lineup.roster[constants.c] , c2)
        self.assertEqual(self.lineup.roster[constants.g] , pg2)
        self.assertEqual(self.lineup.roster[constants.f] , sf2)
        self.assertEqual(self.lineup.roster[constants.flex] , c1)

    def test_add_player(self):
        self.lineup = copy.deepcopy(empty_lineup)
        self.assertEqual(self.lineup.add_player(pg1),0) #this one?
        self.assertEqual(self.lineup.roster[constants.pg], pg1)
        
        self.assertEqual(self.lineup.add_player(pg2),0)
        self.assertEqual(self.lineup.roster[constants.sg], pg2)
        
        self.assertEqual(self.lineup.add_player(sg2),0)
        self.assertEqual(self.lineup.roster[constants.g], sg2)
        
        self.assertEqual(self.lineup.add_player(sg1),0)
        self.assertEqual(self.lineup.roster[constants.flex], sg1)
        
        self.assertEqual(self.lineup.add_player(sf1),0)
        self.assertEqual(self.lineup.roster[constants.sf], sf1)
        
        self.assertEqual(self.lineup.add_player(sf2),0)
        self.assertEqual(self.lineup.roster[constants.pf], sf2)
        
        self.assertEqual(self.lineup.add_player(pf1),0)
        self.assertEqual(self.lineup.roster[constants.f], pf1)

        #print(self.lineup.salary() + pf2.salary)
        #the following 2 lines are just so it doesn't go over salary
        self.lineup.roster[constants.pg] = test_player
        self.lineup.roster[constants.f] 

        self.assertEqual(self.lineup.add_player(pf2), 1)
        self.assertEqual(pf2 in self.lineup.roster.items(), False)

        self.assertEqual(self.lineup.add_player(c1),0)
        self.assertEqual(self.lineup.roster[constants.c], c1)

        self.assertEqual(self.lineup.add_player(pg1),1)
        self.assertEqual(self.lineup.add_player(c2),1)

        expensive_sf = copy.deepcopy(sf1)
        expensive_sf.salary = 42000

        test_salary_cap_lineup = copy.deepcopy(empty_lineup)
        self.assertEqual(test_salary_cap_lineup.add_player(expensive_sf), 0)
        self.assertEqual(test_salary_cap_lineup.roster[constants.sf], expensive_sf)
        
        self.assertEqual(test_salary_cap_lineup.add_player(pg1), 2)
        self.assertEqual(test_salary_cap_lineup.add_player(sg1), 0)


class Test_DFS_Site(unittest.TestCase):
    """tests dk"""

    def setUp(self):
        self.test_dfs_site = DFS_Site(constants.dk)
        self.test_player = copy.deepcopy(test_player)
    
    def test_repr(self):
        representation = self.test_dfs_site.__repr__
        #print(self.test_dfs_site)

    def test_dfs_value(self):
        self.assertEqual(self.test_dfs_site.dfs_value(test_stat_projections,3000),-1.25)

    def test_fantasy_points(self):
        self.assertEqual(self.test_dfs_site.fantasy_points(test_stat_projections),  16.75)
        
        self.test_player.change_stat_projections({
            constants.pts: 0, constants.rbs: 0, constants.asts: 0, constants.stls: 0, constants.blks: 0, constants.tos: 0, constants.threes: 0, constants.dd: 0, constants.td: 0
            })
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections), 0)

        self.test_player.change_stat_projections({constants.pts: 10})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections), 10)
        self.test_player.change_stat_projections({constants.pts: 0})
        
        self.test_player.change_stat_projections({constants.rbs: 10})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections), 12.5)
        self.test_player.change_stat_projections({constants.rbs: 0})

        self.test_player.change_stat_projections({constants.asts: 5})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections),  7.5)
        self.test_player.change_stat_projections({constants.asts: 0})

        self.test_player.change_stat_projections({constants.stls: 5})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections),  10)
        self.test_player.change_stat_projections({constants.stls: 0})

        self.test_player.change_stat_projections({constants.blks: 5})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections),  10)
        self.test_player.change_stat_projections({constants.blks: 0})

        self.test_player.change_stat_projections({constants.tos: 5})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections),  -2.5)
        self.test_player.change_stat_projections({constants.tos: 0})

        self.test_player.change_stat_projections({constants.threes: 5})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections),  2.5)
        self.test_player.change_stat_projections({constants.threes: 0})

        self.test_player.change_stat_projections({constants.dd: 1})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections),  1.5)
        self.test_player.change_stat_projections({constants.dd: 0})

        self.test_player.change_stat_projections({constants.td: 1})
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_player.stat_projections),  3)
        self.test_player.change_stat_projections({constants.td: 0})



if __name__ == '__main__':
    unittest.main()

