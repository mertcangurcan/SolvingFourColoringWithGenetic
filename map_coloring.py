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
	region_groups = create_region_groups(num_of_elements, num_of_regions)
	return region_groups, adjacency_matrix

# printing all color codes for each region
def print_zones(region_groups):
	for i in range (len(region_groups)):
		for j in range (len((region_groups[0]))):
			print("{0}.set Zone {1} color_code : {2}".format(i, j, region_groups[i][j]))

# Creating region groups as randomly colored
def create_region_groups(num_of_elements, num_of_regions):
	region_groups = []
	for i in range (num_of_elements):
		region_groups.append(np.random.randint(0, num_of_regions + 1 , num_of_regions))
	return region_groups

region_groups, neighborhood = initiate_population()
print_zones(region_groups)
# Calculating fitness gradres for each region set
def fitness_function(region_groups, neighborhood_matrix):
	fitness_score = [0] * len(region_groups)
	neighborhood = neighborhood_matrix
	for regions in range(len(region_groups)):
		for i in range(len(neighborhood[0])):
			for j in range(i+1, len(neighborhood)):
				if(neighborhood[i][j] == 1):
					if(region_groups[regions][i] == region_groups[regions][j]):
						fitness_score[regions] -= 10
					if(region_groups[regions][i] != region_groups[regions][j]):
						fitness_score[regions] += 10
	sorted_indexes = np.argsort(fitness_score)
	np.argsort(fitness_score)
	return fitness_score, sorted_indexes

# One point crossover
def one_point_crossover(sorted_indexes, region_groups):
	split_point = np.random.randint(1,len(region_groups[0]))
	# 2 4 
	cross_part_1 = region_groups[sorted_indexes[1]]
	cross_part_2 = region_groups[sorted_indexes[3]]
	region_groups.append(np.concatenate([cross_part_1[:split_point],cross_part_2[split_point:]]))
	region_groups.append(np.concatenate([cross_part_2[:split_point:],cross_part_1[split_point:]]))
	return region_groups
