# -*- coding: utf-8 -*-
"""
Created on Thu May  7 20:34:38 2020

@author: MSI_PC
"""

from mpi4py import MPI
import time

X = [1,2,3,2,3,4,1,3,4,5,1,3,4,5,7,8,2,1,1,4,5,8,2,4,7,9,1]

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
 
class Node: 
    def __init__(self,data): 
        self.data = data 
        self.left = None
        self.right = None
  
 
def insert(root, data): 
  
    if not root: 
        return Node(data) 
  
    if data < root.data: 
        root.left = insert(root.left, data) 
    if data > root.data: 
        root.right = insert(root.right, data) 
       
    return root 
  
  
def find_max(data): 
    root = None
    for i in range(len(data)):
        root = insert(root,data[i])
    current = root 
      
    while(current.right): 
        current = current.right 
    return current.data 

def max_communication(data):
    max = data[0]
    for i in range (len(data)):
        if max < data[i] :
           max = data[i]
           
    return(max)

if rank == 0:
    d1 = X[0:8]
    maxd1 = find_max(d1)
    print("this is rank : " , rank)
    print("this is data X first split")
    print("the maximum value is :", maxd1 )
    shared1 = {'d1':maxd1}
    comm.send(shared1, dest=3)
   

if rank == 1:
    d2 = X[9:17]
    maxd2 = find_max(d2)
    print("this is rank : " , rank)
    print("this is data X second split")
    print("the maximum value is :", maxd2 )
    shared2 = {'d2':maxd2}
    comm.send(shared2, dest=3)
    
if rank == 2:
    d3 = X[18:26]
    maxd3 = find_max(d3)
    print("this is rank : " , rank)
    print("this is data X third split")
    print("the maximum value is :", maxd3 )
    shared3 = {'d3':maxd3}
    comm.send(shared3, dest=3)


if rank == 3:
    receive0 = comm.recv(source=0)
    receive1 = comm.recv(source=1)
    receive2 = comm.recv(source=2)
    num_data = [receive0['d1'],receive1['d2'],receive2['d3']]
    maxdata = max_communication(num_data)
    print("this is the communication result : ")
    print("the maximum data is",maxdata)


#if rank == 0:
#    print("this is rank : " , rank)
#    print("this is data X")
#    print("the maximum value is :", find_max(X))
    
#if rank == 1:
#   print("this is rank : " , rank)
#   print("this is data Y")
#   print("the maximum value is :", find_max(Y))
    
#if rank == 2:
#   print("this is rank : " , rank)
#   print("this is data Z")
#   print("the maximum value is :", find_max(Z)) 
    
    