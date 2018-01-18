dk = 'DRAFTKINGS'
fd = 'FANDUEL'

class DraftKings:

	#right now just dkl
	def __init_(self)
		self.name = name
		self.roster_construction = {
			'PG': ('PG'),
			'SG': ('SG'),
			'SF': ('SF'),
			'PF': ('PF'),
			'C': ('C'),
			'G': ('PG','SG'),
			'F': ('SF','PF'),
			'Flex': ('PG','SG','SF','PF','C'),
			}
		self.salary_cap = 50000
		self.min_proj = 18
		self.value_mult = 4.2
		self.min_sal = 3000

	def value(self,projection,salary):
		return projection - (min_proj + value_mult * (salary - min_sal)/1000)

	def empty_roster():
		return {'PG': None,
				'SG': None,
				'SF': None,
				'PF': None,
				'C': None,
				'G': None,
				'F': None,
				'Flex': None,
				}