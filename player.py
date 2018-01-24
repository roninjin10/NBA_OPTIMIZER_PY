import constants
from site import Site 

class Player:

    def __init__(self, name, team, opp, position, salary, site_id, projection, site= constants.dk):
        self.name = name
        self.team = team
        self.opp = opp
        self.position = position
        self.salary = salary
        self.__site_id = site_id
        self.projection = projection 
        self.site = Site(site)
        
        self.__test_player()

    def __test_player(self):
        """test to make sure it is a valid player"""
        pass

    def projection(self):
        return self.site.fantasy_points(self.projection)

    def site_id(self):
        return __site_id[self.site.site]

    def value(self):
        return self.site.value(self.projection)
