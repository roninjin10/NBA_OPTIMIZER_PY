import pandas as pd

dk = 'DRAFT_KINGS'

def roster_constr(site):
	if site == dk:
		return ([
			['PG'],
			['SG'],
			['SF'],
			['PF'],
			['C'],
			['PG','SG'],
			['SF','PF'],
			['PG','SG','SF','PF','C'],
			])

sal_cap_dk = 50000

def value(site,projection,salary):
	if site == dk:
		min_proj, value_mult, min_sal = 18, 4.2, 3000
	return projection - (min_proj + value_mult * (salary - min_sal)/1000)

def create_pool(site):
	out = pd.read_csv('./projections.csv')[['Name','Projection','Salary','Position','Team']]
	
	out['Value'] = value(site,out['Projection'],out['Salary'])
	for i, roster_spot in enumerate(roster_constr(site)):
		for roster_position in roster_spot:
			out["isEligibleRosterSpot" + str(i)] = True if roster_position in out['Position'] else False
	out["isExcluded"] = False
	out["isLocked"] = True
	out["isInLineup"] = False
	
	return out

if __name__ == "__main__":
	player_pool = create_pool(dk)
	print(player_pool.head())