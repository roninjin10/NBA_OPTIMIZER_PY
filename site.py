
class Site:
    """Site Class currently only supports dk"""    

    def __init_(self, site=dk):
        self.site = site 
        self.roster_construction = dk_roster_constr
        self.sal_cap = dk_sal_cap
        self.minimum_proj = dk_minimum_proj
        self.value_mult = dk_val_mult
        self.min_sal = dk_min_sal

    def value(self,projection,salary):
        return fantasy_points(projection) - (self.min_proj + self.value_mult * (salary - self.min_sal)/1000)

    def empty_roster():
        return dk_empty_roster

    def fantasy_points(player):
        return sum([player.projection[category] * dk_scoring[category] for category in stat_categories])


