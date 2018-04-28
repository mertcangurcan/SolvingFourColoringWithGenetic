import random
import numpy as np
from IPython import embed


# initilazation of first population randomly
def initiate_population():
	num_of_regions = 4;
	all_adjacencies = []
	region_set = []
	for i in range (0,num_of_regions):
		adjacency_matrix = np.random.randint(0,2,(num_of_regions,num_of_regions))
		np.fill_diagonal(adjacency_matrix,0)
		all_adjacencies.append(adjacency_matrix.tolist())
	for i in range (0, 20):
		region_set.append(np.random.randint(0, num_of_regions + 1 , num_of_regions))
	return region_set, all_adjacencies

def print_zones(region_set):
	for i in range (0, len(region_set)):
		for j in range (0, len((region_set[0]))):
			print("{0}.set Zone {1} color_code : {2}".format(i, j, region_set[i][j]))

region_set, neighborhood = initiate_population()
print_zones(region_set)
	
