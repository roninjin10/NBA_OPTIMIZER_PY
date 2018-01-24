from constants import *
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.test_player = Player(name='name', team='team', opp='opp', position='pos', salary=3000, site_id ={dk: '152334'}, projection={'pts' : 10, 'rbs': 1, 'asts': 1, 'stls': 1, 'blks': 1, 'tos': 1, 'threes': 1}, site=dk)
        

    def test_player(self):
        pass

    def test_projection(self):
        self.assertEqual(self.test_player.projection(), 16.75)

    def test_value(self):
        self.assertEqual(self.test_player.value(), -1.25)

if __name__ == '__main__':
    unittest.main()
