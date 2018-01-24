import constants

class DFS_Site:
    """Site Class currently only supports dk"""    

    def __init__(self, dfs_site=constants.dk):
        self.dfs_site = dfs_site 
        self.roster_construction = constants.dk_roster_constr
        self.sal_cap = constants.dk_sal_cap
        self.minimum_proj = constants.dk_minimum_proj
        self.value_mult = constants.dk_val_mult
        self.min_sal = constants.dk_min_sal

    def site_value(self,projection,salary):
        return fantasy_points(projection) - (self.min_proj + self.value_mult * (salary - self.min_sal)/1000)

    def empty_roster():
        return constants.dk_empty_roster

    def fantasy_points(projection):
        return sum([projection[category] * dk_scoring[category] for category in constants.stat_categories])


if __name__ == "__main__":
    print('testing site')
    my_site = DFS_Site(constants.dk)
    print(my_site.dfs_site)
