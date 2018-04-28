import random
import numpy as np

# initilazation of first population randomly
def initiate_population():
	num_of_regions = 4;
	adjacency_matrix = np.random.randint(0,2,(num_of_regions,num_of_regions))
	for i in range (0,num_of_regions):
		adjacency_matrix = np.random.randint(0,2,(num_of_regions,num_of_regions))
		np.fill_diagonal(adjacency_matrix,0)
		all_adjecencies.append(adjacency_matrix.tolist())
	regions = np.random.randint(0, num_of_regions + 1 , num_of_regions)
