from dfs_site import DFS_Site
import constants


def is_shared_element(collection1, collection2):
    """returns true if any elements in 2 collections match.  Used enough where I should make this importable"""
    set1, set2 = set(collection1), set(collection2)
    return len(set1.union(set2)) < len(set1) + len(set2)

class Lineup:
    """lineup class only supports dk atm"""
    """lineup class does not currently support PG/SF.  The plan as of now is to check only specific positions and then
    reinsert the player back into the player pool to check other positions if not taken.  See
    constants.dk_roster_priority for more information"""

    def __init__(self, site_name = constants.dk):

        self.dfs_site = DFS_Site()
        self.roster = self.dfs_site.empty_roster()
    
    def __repr__(self):
        projection = self.dfs_projection()
        salary = self.salary()
        return repr([self.roster[pos].name for pos in self.roster.keys() if not self.roster[pos] is None]) + '/n' + f'Salary: {salary} DFS_Projection: {projection}'

    def __len__(self):
        return len([pos for pos in self.roster.keys() if not self.roster[pos] is None])        

    def salary(self):
        return sum(self.roster[pos].salary for pos in self.roster.keys() if not self.roster[pos] is None)

    def dfs_projection(self):
        return round(sum(self.roster[pos].dfs_projection for pos in self.roster.keys() if not self.roster[pos] is None),2)

    def dic_key(self, current_position, current_player_num):
        return ("Pos: " + str(current_position) + " PlNum: " + str(current_player_num) + " Sal: " + str(self.salary()) + " Positions: " 
            + ''.join(pos + str(self.roster[pos] != None) for pos in constants.dk_roster_order))


    def merge_lineups(self, lineup):
        for pos in self.roster.keys():
        	if self.roster[pos] == None:
        		self.roster[pos] = lineup.roster[pos]


    def erase_lineup(self):
        self.roster = self.dfs_site.empty_roster
        
    def add_player(self, new_player):
        """adds a player to the correct roster spot.
        returns 0 if the add was sucessful
        returns 1 if their is no roster spot for the player
        returns 2 if salary cap constraint would be valuable
        returns another non 0 number if another salary cap constraint is violated"""
        if new_player.salary + self.salary() > self.dfs_site.salary_cap:
            return 2
        #elif (player causes lineup to not satisfy the sites roster construction):
        #   return 3
        else:
            for roster_spot in constants.dk_roster_priority[new_player.position]:
                if self.roster[roster_spot] == None and is_shared_element(new_player.dk_positions(), constants.dk_roster_construction[roster_spot]):
                    self.roster[roster_spot] = new_player
                    return 0
        return 1

