import random
import numpy as np
import sys
import matplotlib.pyplot as plt
import networkx as nx

# initilazation of first population randomly
def initiate_population(num_of_regions):
	num_of_elements = 20
	adjacency_matrix = [[0]*num_of_regions]*num_of_regions
	region_groups = create_region_groups(num_of_elements, num_of_regions)
	
	for i in range(num_of_regions):
		for j in range(num_of_regions):
			if i !=j:
				adjacency_matrix[i][j] = np.random.randint(0, 2)
				adjacency_matrix[j][i] = adjacency_matrix[j][i]
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

# Calculating fitness gradres for each region set
def calculate_fitness(regions_set, neighborhood_matrix):
	fitness_score = 0
	neighborhood = neighborhood_matrix
	for i in range(len(neighborhood[0])):
		for j in range(i+1, len(neighborhood)):
			if(neighborhood[i][j] == 1):
				if regions_set[i] == regions_set[j]:
					fitness_score -= 10
				if regions_set[i] != regions_set[j]:
					fitness_score += 10
	return fitness_score

# One point crossover
def one_point_crossover(first_set, second_set):
	spoint = np.random.randint(1,len(first_set))
	# 2 4
	first_set[spoint:], second_set[spoint:] = second_set[spoint:], first_set[spoint:]
	return first_set, second_set

# 10% chance to mutation of random set
def mutation(region_groups, mutation_delimeter):
	mutation_delimiter = 15
	mutation_chance = np.random.randint(0, 100)
	if mutation_delimiter <= mutation_chance:
		random_set = np.random.randint(0,len(region_groups))
		random_index = np.random.randint(0,len(region_groups[0]))
		random_color = np.random.randint(0,4)
		mutated_set = region_groups[random_set]
		mutated_set[random_index] = random_color
		region_groups.append(mutated_set)
		
# crossover with multipoints between two set
def multi_point_crossover(first_set, second_set):
	spoint_1 = np.random.randint(1,len(first_set))
	spoint_2 = np.random.randint(1, len(first_set) - 1)
	if spoint_2 >= spoint_1:
		spoint_2 += 1
	else: 
		spoint_1, spoint_2 = spoint_2, spoint_1
	
	first_set[spoint_1:spoint_2], second_set[spoint_1:spoint_2] \
		= second_set[spoint_1:spoint_2], first_set[spoint_1:spoint_2]
	return first_set, second_set

# crossover with randomly selected indexes
def uniform_crossover(first_set, second_set, delimeter):
	chance = np.random.randint(0, 100)
	for i in range(len(first_set)):
		if chance <= delimeter:
			first_set[i], second_set[i] = second_set[i], first_set[i]
	return first_set, second_set

# drawing regions as graphs and edges
def draw_regions(result_node, neighborhood):
	color_map = [None] * len(result_node)
	np.array(color_map)
	for i in range(len(result_node)):
        	if result_node[i] == 0:
                	color_map[i] = 'red'
        	elif result_node[i] == 1:
                	color_map[i] = 'blue'
        	elif result_node[i] == 2:
                	color_map[i] = 'yellow'
        	else:
                	color_map[i] = 'green'
	# reordering indexes to represent regions as colors
	for i in range(len(result_node)):
		result_node[i] = i
	
	neighborhood=np.array(neighborhood)
	adjacency_matrix = neighborhood
	rows, cols = np.where(adjacency_matrix == 1)
	edges = zip(rows.tolist(), cols.tolist())
	gr = nx.Graph()
	gr.add_edges_from(edges)
	nx.draw(gr, node_size=500, node_color = color_map, with_labels=True)
	plt.show()

# ----Algorithm running order----
# 1- initiate population
# 2- calculate fitness score
# 3- make selections and crossovers
# 4- mutation
# Repeat n steps

num_of_regions, num_of_steps, mutation_chance = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
region_groups, neighborhood = initiate_population(num_of_regions)
for i in range(num_of_steps):
	fitness_score = []
	for regions_set in region_groups:
        	fitness_score.append(calculate_fitness(regions_set, neighborhood))
	sorted_indexes = np.argsort(fitness_score)[::-1]

	
	child_1 , child_2 = one_point_crossover(region_groups[sorted_indexes[1]], region_groups[sorted_indexes[3]])
	region_groups.append(child_1)
	region_groups.append(child_2)

	# assign and calculate fit func and add again
	child_1, child_2 = multi_point_crossover(region_groups[sorted_indexes[4]], region_groups[sorted_indexes[6]])
	region_groups.append(child_1)
	region_groups.append(child_2)	
	# assign and calculate fit func and add again
	uniform_crossover(region_groups[sorted_indexes[0]],region_groups[sorted_indexes[2]], 25)
	region_groups.append(child_1)
	region_groups.append(child_2)		
	# randomly mutation
	mutation(region_groups, mutation_chance)
	region_groups = region_groups[:100]	
#	print("{0}. Step".format(i))
print(neighborhood)
draw_regions(region_groups[sorted_indexes[0]], neighborhood)

