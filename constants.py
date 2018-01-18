dk = 'DRAFTKINGS'
fd = 'FANDUEL'

pts = 'POINTS'
rbs = 'REBOUNDS'
asts = 'ASTS'
stls = 'STLS'
blks = 'BLKS'
tos = 'TOS'
threes = 'THREES'
dd = 'DOUBLE_DOUBLE'
td = 'TRIPLE_DOUBLE'

pg = 'PG'
sg = 'SG'
sf = 'SF'
pf = 'PF'
c = 'C'
g = 'G'
f = 'F'
flex = 'FLEX'

dk_roster_constr = {
            'PG': ('PG'),
            'SG': ('SG'),
            'SF': ('SF'),
            'PF': ('PF'),
            'C': ('C'),
            'G': ('PG','SG'),
            'F': ('SF','PF'),
            'Flex': ('PG','SG','SF','PF','C'),
            }

dk_empty_roster = {'PG': None,
                'SG': None,
                'SF': None,
                'PF': None,
                'C': None,
                'G': None,
                'F': None,
                'Flex': None,
                }

dk_sal_cap = 50000
dk_minimum_proj = 18
dk_val_mult = 4.2
dk_min_sal = 3000
