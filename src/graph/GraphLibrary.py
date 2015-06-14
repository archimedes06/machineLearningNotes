#an example class in python
import numpy as np;
import igraph as ig;
import numpy as np;
import pandas as pd;
from pylab import *
#random number generator
import random;


#method for generating a random graph with underlying communities
def generateGraph(randomSeed = 1, membershipMatrix = np.array([]) ):
	if (membershipMatrix.size == 0):
		membershipMatrix = np.array([
			[10,0,0],    #user1
			[10,0,0],    #user2
			[10,0,0],    #user3
			[10,1,1],    #user4
			[10,0,0],    #user5
			[0,10,0],    #user6
			[0,10,0],    #user7
			[0,10,0],    #user8
			[0,10,0],    #user9
			[0,10,0],    #user10
			[0,0,10],    #user11
			[0,0,10],    #user12
			[0,0,10],    #user13
			[0,0,10],    #user14
			[0,0,10]     #user15	
		])

	numberNodes = membershipMatrix.shape[0]
	nodeNames = ["{0:0>2}".format(v) for v in range(1,numberNodes+1)]
	#reduction factor, to transform our intuitive membership values (between 0-10) to probabilities.   That is even though two people are
	#only loosely connected to a community (say 3 each), the probability of connection merely due to that shared community would be
	#1-exp(-9) = 99.95%
	connectionModifier = 2.3e-2

	#probability that two nodes are connected... P(i,j) = 1 - exp(connectionStrengths[i,j])
	connectionStrengths = connectionModifier * np.inner(membershipMatrix, membershipMatrix)
	probabiliyOfConnection = 1- np.exp(-connectionStrengths)

	#zeroing the diagonal elements
	np.fill_diagonal(probabiliyOfConnection, 0)

	#probabilityOfConnection contains the probability that any two nodes are connected, given our membership matrix
	#convert this into an actual graph
	dim=probabiliyOfConnection.shape

	#a matrix of random numbers between 0-1;
	#rand(N,M) will create an NxM array of random numbers 
	np.random.seed(1)
	randomProbability = np.random.rand(dim[0], dim[1])

	#constructing the adjacency matrix from any number in the probability grid that is greater than 
	#the corresponding position in the random  
	adjacencyMatrix = probabiliyOfConnection > randomProbability

	communityGraph = ig.Graph.Adjacency(adjacencyMatrix.tolist())
	communityGraph.vs['label'] = nodeNames
	communityGraph.es['weight'] = adjacencyMatrix[adjacencyMatrix.nonzero()]

	return communityGraph