import random
import timeit
import pickle
import matplotlib.pyplot as plt
import math
import sys
import sys
sys.setrecursionlimit(1000000) 

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.size =  1
        self.data = data

# Insert method to create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    self.size=self.size+1
                else:
                    self.left.insert(data)
                    self.size=self.size+1
                    
                    if(self.left.size>(math.ceil(self.size*(float(3)/4)))) : 
                                                                        
                        array_key=[];
                        self.inorder_tree_walk(array_key)     
                        len_array_key=(len(array_key))
                        if(len_array_key % 2)==0:
                            pos_center=int(len_array_key/2)-1
                        else:
                            pos_center=int(len_array_key/2)
                        node_aux=Node(array_key[pos_center])

                        node_aux.balanced_binary_tre(array_key[0:pos_center])
                        
                        node_aux.balanced_binary_tre(array_key[(pos_center+1):len(array_key)])
                        
                        self.data=node_aux.data
                        self.left=node_aux.left
                        self.right=node_aux.right
                        self.size=node_aux.size
                    
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    self.size=self.size+1
                else:
                    self.right.insert(data)
                    self.size=self.size+1
                                        
                    if(self.right.size>(math.ceil(self.size*(float(3)/4)))) : 
                               
                        array_key=[];
                        self.inorder_tree_walk(array_key)     
                        len_array_key=(len(array_key))
                        if(len_array_key % 2)==0:
                            pos_center=int(len_array_key/2)-1
                        else:
                            pos_center=int(len_array_key/2)
                        node_aux=Node(array_key[pos_center])
                        
                        node_aux.balanced_binary_tre(array_key[0:pos_center])
                        
                        node_aux.balanced_binary_tre(array_key[(pos_center+1):len(array_key)])
                        
                        self.data=node_aux.data
                        self.left=node_aux.left
                        self.right=node_aux.right
                        self.size=node_aux.size
                    
        else:
            self.data = data
            self.size= 1

# Insert method to create nodes
    def insert_simple(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    self.size=self.size+1
                else:
                    self.left.insert(data)
                    self.size=self.size+1
                                        
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    self.size=self.size+1
                else:
                    self.right.insert(data)
                    self.size=self.size+1                    
                    
        else:
            self.data = data
            self.size= 1

#Balanced binary tree
    def balanced_binary_tre(self,array_key):
        len_array_key=(len(array_key))
        
        if(len_array_key==1):
            self.insert_simple(array_key[0])
        
        if(len_array_key==2):
            self.insert_simple(array_key[1])
            self.insert_simple(array_key[0])
            
        if(len_array_key>2): 
            if(len_array_key % 2)==0:
                pos_center=int(len_array_key/2)-1
            else:
                pos_center=int(len_array_key/2)            
            self.insert_simple(array_key[pos_center])
                       
            self.balanced_binary_tre(array_key[0:pos_center])
            
            self.balanced_binary_tre(array_key[(pos_center+1):len_array_key])
                        
# inorder tree walk
    def inorder_tree_walk(self,array_key):  
        if self.left is not None:
            self.left.inorder_tree_walk(array_key)
        array_key.append(self.data)
        if self.right is not None:
            self.right.inorder_tree_walk(array_key)
            
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data,self.size)
        if self.right:
            self.right.PrintTree()

def main():
     
    for n in range (1,16):
        print 'n: ',n*1000
        start = timeit.default_timer()
        root = Node(1)        
        for i in range (2,n*1000):
            root.insert(i)
        stop = timeit.default_timer()
        time=stop-start    
        print time
    
if __name__ == '__main__':
    main()


