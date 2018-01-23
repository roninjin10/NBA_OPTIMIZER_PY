import unittest
import dynamic

class TestDynamic(unittest.TestCase):

    def test_init(self):
        test_player = Player(name='name', team='team', opp='opp', pos='pos', salary=1000, real_value =1000, site_id ='152334')
        self.assertEquals(test_player.name, 'name')
        self.assertEquals(test_player.team, 'team')
        self.assertEquals(test_player.opp, 'opp')
        self.assertEquals(test_player.pos, 'pos')
        self.assertEquals(test_player.salary, 1000)
        self.assertEquals(test_player.real_value, 1000)
        self.assertEquals(test_player.site_id , '152334')

    
	        	


if __name__ == '__main__':
    unittest.main()
    
