import constants
from player import Player
import unittest


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.test_player = Player(name='name', team='team', opp='opp', position='pos', salary=3000, dfs_site_id ={constants.dk: '152334'}, stat_projections={constants.pts : 10, constants.rbs: 1, constants.asts: 1, constants.stls: 1, constants.blks: 1, constants.tos: 1, constants.threes: 1, constants.dd: 0, constants.td: 0}, dfs_site=constants.dk)
        

    def test_player(self):
        pass

    def test_projection(self):
        self.assertEqual(self.test_player.dfs_projection(), 16.75)

    def test_value(self):
        self.assertEqual(self.test_player.site_value(), -1.25)

if __name__ == '__main__':
    unittest.main()
