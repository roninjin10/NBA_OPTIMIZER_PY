from dfs_site import DFS_Site

class Lineup:

    def __init__(self):

        self.site = DFS_Site()
        self.roster = self.site.empty_roster

    #need to update the roster if site changes
    def set_site(self, new_site):
        pass

    def salary(self):
        return sum(plr.salary for plr in self.roster.items() if not plr is None)

    def points(self):
        return sum(self.site.fantasy_points(plr) for plr in self.roster.items() if not plr is None)

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
        #adds a player to a lineup to a specified roster_spot. Overwrites player if roster_spot specified
        # If roster_spot is not given, it puts the player in the valid, empty roster spot that provides most future roster flexibility
        # method returns a boolean based on if the player was added or not
        if roster_spot != None:
            self.roster[roster_spot] = new_player


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

    def copy_lineup(self):
        #returns a copy of the same lineup
        out = Lineup()
        out.roster = self.roster
        return out
