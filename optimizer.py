class Optimizer:

	def __init__(self, site, pool, lineups=[]):
		self.site = Site(site)
		self.pool = pool
		self.lineups = lineups

	def dynamic_optimizer(self, n):
		pass

	def genetic_optimizer(self, n):
		pass

	def hybrid_optimizer(self, n):
		pass

	def rust_dynamic_optimizer(self, n):
		pass

	def rust_hybrid_optimizer(self, n):
		pass