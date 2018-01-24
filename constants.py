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

stat_categories = (pts, rbs, asts, stls, blks, tos, threes, dd, td)

#DraftKings Constants

dk_roster_constr = {
            PG: ('PG'),
            SG: ('SG'),
            SF: ('SF'),
            PF: ('PF'),
            C: ('C'),
            G: ('PG','SG'),
            F: ('SF','PF'),
            Flex: ('PG','SG','SF','PF','C'),
            }


dk_empty_roster = {
            PG: None,
            SG: None,
            SF: None,
            PF: None,
            C: None,
            G: None,
            F: None,
            Flex: None,
            }

dk_scoring = {
    pts: 1
    rbs: 1.25
    asts: 1.5
    stls: 2
    blks: 2
    tos: -.5
    threes: .5
    dd: 1.5
    td: 3
    }

dk_sal_cap = 50000
dk_minimum_proj = 18
dk_val_mult = 4.2
dk_min_sal = 3000

def empty_roster(site):
    if site == dk:
        return dk_empty_roster