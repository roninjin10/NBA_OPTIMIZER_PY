
class Site:

    def __init_(self)
        self.name = name
        self.roster_construction = dk_roster_constr
        self.sal_cap = dk_sal_cap
        self.minimum_proj = dk_minimum_proj
        self.value_mult = dk_val_mult
        self.min_sal = dk_min_sal

    def value(self,projection,salary):
        return projection - (self.min_proj + self.value_mult * (salary - self.min_sal)/1000)

    def empty_roster():
        return dk_empty_roster

    #calculates fantasy points of Player object
    def fantasy_points(player):
        return sum([player[category] * dk_scoring[category] for category in dk_scoring.keys()])