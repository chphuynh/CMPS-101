#!/usr/bin/env python3
# Christopher Huynh chphuynh
# Oliver Rene orene

import numpy as np
import math

def selectionsort(A):
   n = A.size
   for i in range(0,n): #iterates through the array
      minA = A[i]
      minInd = i
      for j in range(i,n): #iterates through remaining n-i items of array
         if A[j] < minA: #Swaps A[j] with the minimum element if A[j] is less than the minimum
            minA = A[j]
            minInd = j
      A[minInd] = A[i]
      A[i] = minA
   return A #returns the sorted array

def insertionsort(A):
   n = A.size
   for i in range(1,n): #iterates through the array
      j = i
      while (j > 0) and ( A[j-1] > A[j]): #Swaps all values until A[0..i] is sorted
         tmp = A[j]
         A[j] = A[j-1]
         A[j-1] = tmp
         j -= 1
   return A #returns the sorted array.

def merge(B, C):
   D = np.empty(B.size + C.size, dtype = B.dtype) #creates an array of the total size of B and C if merged
   B = np.append(B,np.inf)  #Pushes infinity to the end of B
   C = np.append(C,np.inf)  #Pushes infinity to the end of C
   i = j = k = 0
   while (B[i] < np.inf) | (C[j] < np.inf): #Checks while the values are less than infinity
      if (B[i] <  C[j]): 
         D[k] = B[i]  #Pushes B[i] to D if it is less than C[j]
         i = i + 1    #Increment i
      else:
         D[k] = C[j]  #Pushes C[j] to D if it is less than C[j]
         j = j + 1    #Increment J
      k = k + 1
   return D

def mergesort(A):
   if (A.size <= 1):  #Base Case for recursion: An array of size 1 or 0 is trivially sorted
      return A
   mid = int(A.size/2)  #Finds the approximate midpoint of A
   L = A[:mid]  #Splits the array A into too arrays L and R split from the middle
   R = A[mid:]
   sortL = mergesort(L) #recursively run mergesort on L
   sortR = mergesort(R) #recursively run mergesort on R
   return merge(sortL,sortR) #Merges the two recursively sorted arrays

