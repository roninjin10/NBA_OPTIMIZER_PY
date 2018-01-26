import constants
from player import Player
from dfs_site import DFS_Site
import unittest
from lineup import Lineup
import copy

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
        self.lineup = Lineup()
        
    def test_salary(self):
        self.assertEqual(self.lineup.salary, 0)

        self.lineup.roster[constants.pg] = pg1
        self.assertEqual(self.lineup.salary,9000)

        self.lineup.roster[constants.sg] = sg1
        self.assertEqual(self.lineup.salary, 17000) 

    def test_dfs_projection(self):
        self.assertEqual(self.lineup.dfs_projection, 0)

        self.lineup.roster[constants.pg] = pg1
        self.assertEqual(self.lineup.dfs_projection, 42.8)
        
        self.lineup.roster[constants.sg] = sg1
        self.assertEqual(self.lineup.dfs_projection, 76.5)

    def test_key(self):
        pass
  
 
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
