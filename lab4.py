import random
import timeit
import pickle
import matplotlib.pyplot as plt
import math
import sys
import sys
sys.setrecursionlimit(1000000) 

#retorna o menor elemnto do arry  recurso similar ao quicksort

def k_small_element_quick(arr, l, r, k): 
  
    if (k > 0 and k <= r - l + 1):       
        pos = partition(arr, l, r)         
        if (pos - l == k - 1): 
            return arr[pos] 
        if (pos - l > k - 1):  
            return k_small_element_quick(arr, l, pos - 1, k)   
        return k_small_element_quick(arr, pos + 1, r, k - pos + l - 1)   
    return sys.maxsize 
  

def partition(arr, l, r): 
  
    x = arr[r] 
    i = l 
    for j in range(l, r): 
        if (arr[j] <= x): 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
    arr[i], arr[r] = arr[r], arr[i] 
    return i 
  
  
#retorna o menor elemnto do arry  usando heapsort
  
def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        heapify(arr, n, largest) 
  
def heapSort(arr): 
    n = len(arr) 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0)   
  
def kthSmallest_heapsort(arr, n, k): 
    heapSort(arr)
    return arr[k-1] 
  
#retorna o menor elemnto do arry  usando max heap

class MaxHeap:
    def __init__(self,a,size):
        self.harr=a
        self.capacity=0
        self.heap_size=size
        
    def MaxHeap(self,a,size):
        self.heap_size = size
        self.harr = a
        i = (self.heap_size - 1)/2; 
        while (i >= 0) :
            self.maxHeapify(i) 
            i=i-1
        
    def maxHeapify(self,i):
        l = self.left(i)
        r = self.right(i)
        m = i; 
        if (l < self.heap_size and self.harr[i] < self.harr[l]) :
            m = l
        if (r < self.heap_size and self.harr[m] > self.harr[r]) :
            m = r 
        if (m != i) :
            [self.harr[m], self.harr[i]]=swap(self.harr[m], self.harr[i]) 
            self.maxHeapify(m)         
        
    def parent(self,i):
        return (i-1)/2 
        
    def left(self,i):
        return (2*i + 1) 
        
    def right(self,i): 
        return (2*i + 2)   
        
    def extractMax(self):
        if (self.heap_size == 0) :
            return -1   
        m = self.harr[0];           
        self.harr[0] = self.harr[self.heap_size-1] 
        self.maxHeapify(0)
        return m;       
        
    def getMax(self):
        return self.harr[0]  
        
    def replaceMax(self,x):
        self.harr[0] = x
        self.maxHeapify(0)

def swap (x,y):
    temp=x
    x=y
    y=temp
    return x,y

def k_small_element_heap(arr, n, k):     
    mh=MaxHeap(arr,k)
    for i in range (1,n):
        mh.extractMax()    
    return mh.extractMax()
    
#retorna o menor elemento do array usando select

def kthSmallest_select(arr, l, r, k): 
	
	if (k > 0 and k <= r - l + 1): 
		n = r - l + 1
		median = [] 
		i = 0
		while (i < n // 5): 
			median.append(findMedian(arr, l + i * 5, 5)) 
			i += 1
		if (i * 5 < n): 
			median.append(findMedian(arr, l + i * 5, n % 5)) 
			i += 1
		if i == 1: 
			medOfMed = median[i - 1] 
		else: 
			medOfMed = kthSmallest_select(median, 0,i - 1, i // 2)  
		pos = partitionS(arr, l, r, medOfMed) 
		if (pos - l == k - 1): 
			return arr[pos] 
		if (pos - l > k - 1): 
			return kthSmallest_select(arr, l, pos - 1, k)  
		return kthSmallest_select(arr, pos + 1, r,k - pos + l - 1) 
	return sys.maxsize

def swaps(arr, a, b): 
	temp = arr[a] 
	arr[a] = arr[b] 
	arr[b] = temp 

#procura x em arr e particiona arr em funcao de x
def partitionS(arr, l, r, x): 
	for i in range(l, r): 
		if arr[i] == x: 
			swaps(arr, r, i) 
			break

	x = arr[r] 
	i = l 
	for j in range(l, r): 
		if (arr[j] <= x): 
			swaps(arr, i, j) 
			i += 1
	swaps(arr, i, r) 
	return i 

# buscando a mediana do arrar do indice i ate 1+n
def findMedian(arr, l, n): 
    lis = [] 
    for i in range(l, l + n): 
        lis.append(arr[i]) 
    lis.sort() 
    return lis[n // 2] 
    

def main():
    

    arr=[]
    tamVector=999999
    #tamVector=90111000
    for i in range(1,tamVector*21):
        x = random.randint(-99999,99999)
        arr.append(x)
    print len(arr)
  
    with open('vector.file', 'w') as f:
        pickle.dump(arr, f)
    #with open('vector.file', 'r') as f:
    #    arr = pickle.load(f)
	
    arrAux=[]
    stoogeSortTime=[]
    x=[]
    k_vet=[1,32,1024,32768,1048576,33554432,1073741824,1073741824,34359738368,1099511627776,35184372088832,1125899906842624,36028797018963968,1152921504606846976,36893488147419103232L,1180591620717411303424L,37778931862957161709568L,1208925819614629174706176L,38685626227668133590597632L,1237940039285380274899124224L,39614081257132168796771975168L,1267650600228229401496703205376L]
    k=k_vet[1]
    for  i in range(1,21):
        arrAux=arr[1:i*tamVector+1+i]          
        x.append(len(arrAux))
        print len(arrAux)  
        arrAux2=arrAux
        for j in k_vet: 
            arrAux=arrAux2
            if(j<len(arrAux)):
                k=j
            else:
                break
            print(" K: ", k) 
            
            start = timeit.default_timer()
                    
            print(" quicksort K'th smallest element is")
            y=k_small_element_quick(arrAux, 0, len(arrAux) - 1, k)
            
            #print(" max heap K'th smallest element is")
            #y=k_small_element_heap(arrAux,len(arrAux),k)
            
            #print(" heapsort K'th smallest element is")
            #y=kthSmallest_heapsort(arrAux,len(arrAux),k) 
            
            print(" select algorithm  K'th smallest element is")
            y= kthSmallest_select(arrAux,0,len(arrAux)-1,k)
                    
            stop = timeit.default_timer()
            time=stop-start
            stoogeSortTime.append(time)
            #print 'MaxSubarraySum o(n2)'        
            #print 'MaxSubarraySum o(nlogn)'
            #print 'MaxSubarraySum o(n) recursive'
            #print 'MaxSubarraySum o(n) '
            print(" K: ", k) 
            print time
        
     
    
if __name__ == '__main__':
    main()


