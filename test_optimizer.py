import constants
from player import Player
from dfs_site import DFS_Site
import unittest

test_stat_projections = {constants.pts : 10, constants.rbs: 1, constants.asts: 1, constants.stls: 1, constants.blks: 1, constants.tos: 1, constants.threes: 1, constants.dd: 0, constants.td: 0}  

test_player = Player(name='name', team='team', opp='opp', position='pos', salary=3000, dfs_site_id ={constants.dk: '152334'}, stat_projections=test_stat_projections, dfs_site=constants.dk)
 


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.test_player = test_player       

    def test_player(self):
        pass

    def test_dfs_projection(self):
        self.assertEqual(self.test_player.dfs_projection(), 16.75)

    def test_value(self):
        self.assertEqual(self.test_player.dfs_value(), -1.25)


class TestDFS_Site(unittest.TestCase):

    def setUp(self):
        self.test_dfs_site = DFS_Site(constants.dk)
        self.test_player = test_player
        self.test_stat_projections = test_stat_projections
    
    def tearDown(self):
        self.test_stat_projections = test_stat_projections

    def test_dfs_value(self):
        self.assertEqual(self.test_dfs_site.dfs_value(self.test_stat_projections, 3000),-1.25)

    def test_fantasy_points(self):
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections),  16.75)
        
        self.test_stat_projections = {constants.pts : 0, constants.rbs: 0, constants.asts: 0, constants.stls: 0, constants.blks: 0, constants.tos: 0, constants.threes: 0, constants.dd: 0, constants.td: 0}
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections), 0)

        self.test_stat_projections[constants.pts] = 10
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections), 10)
        self.test_stat_projections[constants.pts] = 0
        
        self.test_stat_projections[constants.rbs] = 10
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections), 12.5)
        self.test_stat_projections[constants.rbs] = 0

        self.test_stat_projections[constants.asts] = 10
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections),  15)
        self.test_stat_projections[constants.asts] = 0

        self.test_stat_projections[constants.stls] = 5
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections),  10)
        self.test_stat_projections[constants.stls] = 0

        self.test_stat_projections[constants.blks] = 5
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections),  10)
        self.test_stat_projections[constants.blks] = 0

        self.test_stat_projections[constants.tos] = 5
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections),  -2.5)
        self.test_stat_projections[constants.tos] = 0

        self.test_stat_projections[constants.threes] = 5
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections),  2.5)
        self.test_stat_projections[constants.threes] = 0

        self.test_stat_projections[constants.dd] = 1
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections),  1.5)
        self.test_stat_projections[constants.dd] = 0

        self.test_stat_projections[constants.td] = 1
        self.assertEqual(self.test_dfs_site.fantasy_points(self.test_stat_projections),  3)
        self.test_stat_projections[constants.td] = 0



if __name__ == '__main__':
    unittest.main()
