import random
import timeit
import pickle
import matplotlib.pyplot as plt

#-----------------------insertionSort-----------------------#
def insertionSort(arr): 
    for i in range(1, len(arr)):   
        key = arr[i]   
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
		
#-----------------------mergeSort-----------------------#
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Encontrando o metade do vetor
        L = arr[:mid] # Dividindo os elementos do vetor 
        R = arr[mid:] # em 2 partes 
        mergeSort(L) # Classificando a primeira metade
        mergeSort(R) # Classificando a segunda metade 
        i = j = k = 0          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1          
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1  
#-----------------------heapSort-----------------------#
def heapify(arr, n, i): 
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2       
    if l < n and arr[i] < arr[l]: 
        largest = l   
    if r < n and arr[largest] < arr[r]: 
        largest = r   
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]   
        heapify(arr, n, largest) 		
def heapSort(arr): 
    n = len(arr)   
    for i in range(n, -1, -1): 
        heapify(arr, n, i)   
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 		
		
#-----------------------main-----------------------#  

def main():
    #print("This is a main function")
    #arr = randint(1, 10000^2)  
    arr=[]
    tamVector=9999
    for i in range(1,tamVector*21):
        x = random.randint(1,9999999999)
        arr.append(x)
    print len(arr)
  
    with open('vector.file', 'w') as f:
        pickle.dump(arr, f)
    #with open('vector.file', 'r') as f:
    #    arr = pickle.load(f)
	
    arrAux=[]
    insertionSortTime=[]
    mergeSortTime=[]
    heapSortTime=[]
    x=[]
    for  i in range(1,21):
        arrAux=arr[1:i*tamVector+1+i]          
        x.append(len(arrAux))
        print len(arrAux)
        
        start = timeit.default_timer()
        insertionSort(arrAux)
        stop = timeit.default_timer()
        time=stop-start
        insertionSortTime.append(time)
        print 'insertionSort'        
        print time
        '''
        start = timeit.default_timer()
        mergeSort(arrAux) 
        stop = timeit.default_timer()
        time=stop-start
        mergeSortTime.append(stop-start)
        print 'mergeSort'        
        print time
        
        start = timeit.default_timer()
        heapSort(arrAux) 
        stop = timeit.default_timer()
        time=stop-start
        heapSortTime.append(stop-start)
        print 'heapSort'        
        print time'''
        
    #x=range(1,20)
    print len(insertionSortTime)
    print len(x)
    plt.plot(x,insertionSortTime,'ro')
    #(x,insertionSortTime,'ro',(x,mergeSortTime,'r--',x,heapSortTime,'bs',)
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo gasto')
    plt.title('Tempo do insertion sort')
    plt.show()
    
if __name__ == '__main__':
    main()


