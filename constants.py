
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

dk_roster_order = [pg, sg, sf, pf, c, g, f, flex]

dk_roster_priority = {
            'PG': [pg, g, flex],
            'PG/SG': [pg, sg, g, flex],
            'PG/SF1': [pg],
            'SG': [sg, g, flex],
            'SG/SF': [sg, g, sf, f, flex],
            'PG/SF2': [g],
            'SF': [sf, f, flex],
            'SF/PF': [sf, pf, f, flex],
            'PG/SF3': [sf],
            'PF': [pf, f, flex],
            'PF/C': [pf, f, c, flex],
            'PG/SF4': [f, flex],
            'C': [c, flex],
            }

dk_roster_constr = { 
            pg: ('PG'),
            sg: ('SG'),
            sf: ('SF'),
            pf: ('PF'),
            c: ('C'),
            g: ('PG','SG'),
            f: ('SF','PF'),
            flex: ('PG','SG','SF','PF','C'),
            }


dk_empty_roster = {
            pg: None,
            sg: None,
            sf: None,
            pf: None,
            c: None,
            g: None,
            f: None,
            flex: None,
            }

dk_scoring = {
    pts: 1,
    rbs: 1.25,
    asts: 1.5,
    stls: 2,
    blks: 2,
    tos: -.5,
    threes: .5,
    dd: 1.5,
    td: 3,
    }

dk_sal_cap = 50000
dk_min_proj = 18
dk_val_mult = 4.2
dk_min_sal = 3000

def empty_roster(site):
    if site == dk:
        return dk_empty_roster
