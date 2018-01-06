import pandas as pd
import numpy as np 

dk = 'DRAFT_KINGS'

def roster_constr(site):
	if site == dk:
		return [
			['PG'],
			['SG'],
			['SF'],
			['PF'],
			['C'],
			['PG','SG'],
			['SF','PF'],
			['PG','SG','SF','PF','C'],
			]

sal_cap_dk = 50000

def value(site,projection,salary):
	if site == dk:
		min_proj, value_mult, min_sal = 18, 4.2, 3000

	return projection - (min_proj + value_mult * (salary - min_sal)/1000)

def create_pool(site):

	out = pd.read_csv('./projections.csv')[['Name','Projection','Salary','Position','Team']]
	
	out['Value'] = value(site,out['Projection'],out['Salary'])

	for i, roster_spot in enumerate(roster_constr(site)):
		out["isEligibleRosterSpot" + str(i)] = False
		for roster_position in roster_spot:
			out["isEligibleRosterSpot" + str(i)] = np.logical_or(out['Position'].str.contains(roster_position) , out["isEligibleRosterSpot" + str(i)])
	
	out["isExcluded"] = False
	out["isLocked"] = False
	out["isInLineup"] = False
	
	return out

if __name__ == "__main__":
	player_pool = create_pool(dk)
	print(player_pool.head())