import copy

class __Optimizer:

	def __init__(self, site=dk, pool=None, lineups=[]):
		self.site = Site(site)
		self.pool = pool
		self.lineups = lineups
		self.memoized = {}

		if self.pool == None:
			pool = Pool()

        def __len__(self):
            return len(lineups)

        def __repr__(self):
            return repr(lineups)

        def __getitem__(self, key):
            return lineups[key]


class Dynamic_Optimizer(__Optimizer):

	def __recursive_step(self, cur_lineup, cur_position, cur_player):
		if cur_lineup.is_valid_lineup:
			return cur_lineup


		lineup_key = cur_lineup.key(cur_position, cur_player)
		if lineup_key in self.memoized.keys:
			return cur_lineup.merge_lineup(self.memoized[lineup_key])

		lineup_if_pass = __dynamic_optimizer(copy.deepcopy(cur_lineup), cur_position, cur_player + 1)

		lineup_if_take = __dynamic_optimizer(copy.deepcopy(cur_lineup).add_player(self.lineups[cur_player]), cur_position + 1, 0)

		if lineup_if_pass == None or lineup_if_take == None:
			return lineup_if_pass if lineup_if_take == None else lineup_if_take
		return lineup_if_pass if lineup_if_pass.salary > lineup_if_take.salary else lineup_if_take

	def optimize(self, n):
		self.memoized = {}
		self.lineups.append( __dynamic_optimizer(empty_roster(self.site), 0, 0))

class Genetic_Optimizer(__Optimizer):

	def optimize(self, n):
            pass
