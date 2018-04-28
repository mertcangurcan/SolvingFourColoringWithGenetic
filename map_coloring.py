import random
import numpy as np
from IPython import embed


# initilazation of first population randomly
def initiate_population():
	num_of_regions = 4
	num_of_elements = 20
	all_adjacencies = []
	adjacency_matrix = np.random.randint(0,2,(num_of_regions,num_of_regions))
	np.fill_diagonal(adjacency_matrix,0)
	region_set = create_region_set(num_of_elements, num_of_regions)
	return region_set, adjacency_matrix

def print_zones(region_set):
	for i in range (0, len(region_set)):
		for j in range (0, len((region_set[0]))):
			print("{0}.set Zone {1} color_code : {2}".format(i, j, region_set[i][j]))
def create_region_set(num_of_elements, num_of_regions):
	region_set = []
	for i in range (0, num_of_elements):
		region_set.append(np.random.randint(0, num_of_regions + 1 , num_of_regions))
	return region_set

region_set, neighborhood = initiate_population()
print_zones(region_set)
