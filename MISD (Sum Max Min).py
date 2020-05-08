# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:02:31 2020

@author: MSI_PC
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size


X = [1,2,3,2,3,4,1,3,4]

A = X[0]
B = X[0]
C = 0

def find_max(X):
    global A
    for i in range (len(X)):
        if A < X[i] :
           A = X[i]
           
    return(A)

def find_min(X):
    global B
    for i in range (len(X)):
        if B > X[i] :
           B = X[i]
           
    return(B)
    
def find_sum(X):
    global C
    for i in range (len(X)):
           C = C + X[i]
           
    return(C)


if rank == 0:
    print("this is rank : " , rank)
    print("the maximum value is : ", find_max(X))
    
if rank == 1:
   print("this is rank : " , rank)
   print("the minimum value is : ", find_min(X))
    
if rank == 2:
   print("this is rank : " , rank)
   print("the sum value is : ", find_sum(X))


    
    