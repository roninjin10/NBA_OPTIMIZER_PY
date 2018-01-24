import constants
from dfs_site import DFS_Site 

class Player:

    def __init__(self, name, team, opp, position, salary, dfs_site_id, stat_projections, dfs_site= constants.dk):
        self.name = name
        self.team = team
        self.opp = opp
        self.position = position
        self.salary = salary
        self.__dfs_site_id = dfs_site_id
        self.stat_projections = stat_projections
        self.dfs_site = DFS_Site(dfs_site)
        
    def dfs_projection(self):
        return self.dfs_site.fantasy_points(self.stat_projections)
    
    def site_value(self):
        return self.dfs_site.site_value(self.stat_projections, self.salary)

    def dfs_site_id(self):
        return __site_id[self.dfs_site.dfs_site]

    def value(self):
        return self.dfs_site.value(self.projection)
