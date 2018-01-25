import constants
from dfs_site import DFS_Site 

class Player:

    def __init__(self, name, team, opp, position, salary, dfs_site_id, stat_projections, site_name= constants.dk):
        self.name = name
        self.team = team
        self.opp = opp
        self.position = position
        self.salary = salary
        self.dfs_site_id = dfs_site_id
        self.stat_projections = stat_projections
        self.site_name = site_name

        dfs_site = DFS_Site(site_name)
        
        self.dfs_projection = dfs_site.fantasy_points(self.stat_projections)
        self.dfs_value = dfs_site.dfs_value(self.stat_projections, self.salary)        

    def __repr__(self):
        dic = {
            'Name': self.name,
            'Salary': self.salary,
            f'{self.site_name}_Projection': self.dfs_projection,
            f'{self.site_name}_Value': self.dfs_value,
            'Team': self.team,
            'Opp': self.opp,
            'Position': self.position,
            f'{self.site_name}_ID': self.dfs_site_id,
            }
        return dic.__repr__()
 
    def change_site(self, position, salary, dfs_site_id, site_name):
        self.position = position
        self.salary = salary
        self.dfs_site_id = dfs_site_id
        self.site_name = site_name

        dfs_site = DFS_Site(site_name)
        
        self.dfs_projection = dfs_site.fantasy_points(self.stat_projections)
        self.dfs_value = dfs_site.dfs_value(self.stat_projection, self.salary)

    def change_stat_projections(self, new_stat_projections):
        for category in new_stat_projections.keys():
            self.stat_projections[category] = new_stat_projections[category]
        
        dfs_site = DFS_Site(self.site_name)

        self.dfs_projection = dfs_site.fantasy_points(self.stat_projections)
        self.dfs_value = dfs_site.dfs_value(self.stat_projections, self.salary)

    def dk_positions(self):
        return self.position.split('/')
    
    def full_site_id(self):
        return self.name + ' (' + str(self.dfs_site_id) + ')'
