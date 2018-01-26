import constants

class DFS_Site:
    """Site Class currently only supports dk"""    

    def __init__(self, dfs_site=constants.dk):
        self.dfs_site = dfs_site 
        self.roster_construction = constants.dk_roster_constr
        self.salary_cap = constants.dk_sal_cap
        self.min_proj = constants.dk_min_proj
        self.value_mult = constants.dk_val_mult
        self.min_sal = constants.dk_min_sal
    
    def __repr__(self):
        return f'Site Name: {self.dfs_site} Salary Cap: {self.sal_cap}'    

    def dfs_value(self,projection,salary):
        return self.fantasy_points(projection) - (self.min_proj + self.value_mult * (salary - self.min_sal)/1000)

    def empty_roster(self):
        return constants.dk_empty_roster

    def fantasy_points(self, projection):
        return sum([projection[category] * constants.dk_scoring[category] for category in constants.stat_categories])


if __name__ == "__main__":
    print('testing site')
    my_site = DFS_Site(constants.dk)
    print(my_site.dfs_site)
