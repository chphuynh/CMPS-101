#!/usr/bin/env python3
# Christopher Huynh chphuynh
# Oliver Rene orene

import numpy as np
import math

def matmult(A, x):
	n = x.size
	#create empty array
	b = np.empty(n)
	for i in range(0,n): #iterates through matrix
		summation = 0
		for j in range(0,n):
			#multiplies each column of A[i] by each column of x
			step = A[i][j] * x[j]
			summation = summation + step
		#puts value in array
		b[i] = int(summation)
	return b

def hadmat(k):
	n = 2 ** k
	# returns the base case of H_2
	if(n == 2):
		return np.array([[1,1],[1,-1]])
	#forms H_n through the definition given of a Hadamard Matrix
	tmp = np.concatenate(np.array([[hadmat(k-1),hadmat(k-1)],[hadmat(k-1),-(hadmat(k-1))]]),axis=1)
	return np.concatenate(tmp,axis=1)

def hadmatmult(H, x):
	n = x.size
	if(n == 2):
		return np.array([[x[0]+x[1]],[x[0]-x[1]]])
	#Split H into 4 quadrants
	A = np.hsplit(H, 2)
	A[0] = np.vsplit(A[0], 2)
	#Using quadrant I, recursively run hadmatmult on x[0..n/2] and x[n/2+1..n]
	blockX1 = hadmatmult(A[0][0],x[0:int(n/2)])
	blockX2 = hadmatmult(A[0][0],x[int(n/2):n])
	#return the divide and conquer of H_n as given in equation 2
	return np.array([[blockX1 + blockX2],[blockX1 - blockX2]]).flatten()