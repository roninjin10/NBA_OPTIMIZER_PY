from dfs_site import DFS_Site
import constants

def is_shared_element(collection1, collection2):
    """returns true if any elements in 2 collections match.  Used enough where I should make this importable"""
    set1, set2 = set(collection1), set(collection2)
    return len(set1.union(set2)) < len(set1) + len(set2))

class Lineup:

    def __init__(self, site_name = constants.dk):

        self.site = DFS_Site()
        self.roster = self.site.empty_roster
    
    def __repr__(self):
        projection = self.dfs_projection()
        salary = self.salary()
        return self.roster.__repr__ + '/n' + f'Salary: {salary} DFS_Projection: {projection}'

    def __len__(self):
        return len(plr for plr in self.roster.items() if not plr is None)        

    def salary(self):
        return sum(plr.salary for plr in self.roster.items() if not plr is None)

    def dfs_projection(self):
        return sum(plr.dfs_projection for plr in self.roster.items() if not plr is None)

    def key(self, current_position, current_player_num):
        return "Pos: " + current_position + " PlNum: " + current_player_num + " Sal: " + str(self.salary()) + " Positions: " + ''.join(str(pos != None) for pos in self.roster.items())


    def merge_lineup(self, lineup):
        for pos in self.roster.keys():
        	if self[pos] == None:
        		self[pos] = lineup[pos]

    def erase_lineup(self):
        for pos in self.roster.keys():
        	self[pos] = None

    def add_player(self, new_player, roster_spot=None):
        """adds a player to the correct roster spot.
        returns 0 if the add was sucessful
        returns 1 if their is no roster spot for the player
        returns 2 if salary cap constraint would be valuable
        returns another non 0 number if another salary cap constraint is violated"""
        if new_player.salary + self.salary() > self.site.salary_cap:
            return 2
        #elif (player causes lineup to not satisfy the sites roster construction):
        #   return 3
        else:
            for roster_spot in [constants.pg, constants.sg, constants.sf, constants.pf, constants.c, constants.g, constants.f, constants.f]:
                if self.roster[roster_spot] != None and is_shared_element(new_player.dk_position(), dk_roster_construction[roster_spot]):
                    self.roster[roster_spot] = new_player
                    return 0
        return 1




    ####the below methods I am unsure if necessary###

    def is_valid_salary(self):
        return self.salary() <= self.site.sal_cap

    #this likely should be moved to the Sites class since it's site specific
    def is_valid_team(self):
        team_opponent = []
        for plr in self.roster.items():
            if team_opponent == []:
                team_opponent.append(plr.get_info('team'))
                team_opponent.append(plr.get_info('opp'))
            else:
                if not plr.get_info('team') in team_opponent:
                    return True
        return False

    #not sure if this is necessary
    def is_valid_positional(self):
        #returns boolean based on if the lineup has every position filled
        for plr in self.roster.items():
            if plr is None:
                return False
        return True

    def is_valid(self):
        return self.is_valid_positional() and self.is_valid_salary() and self.is_valid_team()

