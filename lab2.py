import random
import timeit
import pickle
import matplotlib.pyplot as plt

#-----------------------Stooge sorte-----------------------#

def stoogesort(arr, l, h):
    if l >= h:
        return
    if arr[l]>arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t
    if h-l+1 > 2:
        t = (int)((h-l+1)/3)
        stoogesort(arr, l, (h-t))
        stoogesort(arr, l+t, (h))
        stoogesort(arr, l, (h-t))
        
#-----------------------main-----------------------#  

def main():
    #print("This is a main function")
    #arr = randint(1, 10000^2)  
    arr=[]
    tamVector=99
    for i in range(1,tamVector*21):
        x = random.randint(1,999)
        arr.append(x)
    print len(arr)
  
    with open('vector.file', 'w') as f:
        pickle.dump(arr, f)
    #with open('vector.file', 'r') as f:
    #    arr = pickle.load(f)
	
    arrAux=[]
    stoogeSortTime=[]
    x=[]
    for  i in range(1,21):
        arrAux=arr[1:i*tamVector+1+i]          
        x.append(len(arrAux))
        print len(arrAux)        
        start = timeit.default_timer()
        stoogesort(arrAux,0,len(arrAux)-1)
        stop = timeit.default_timer()
        time=stop-start
        stoogeSortTime.append(time)
        print 'stoogeSort'        
        print time
        
        
    #x=range(1,20)
    print len(stoogeSortTime)
    print len(x)
    plt.plot(x,stoogeSortTime,'ro')
    #(x,stoogeSortTime,'ro',(x,mergeSortTime,'r--',x,heapSortTime,'bs',)
    plt.xlabel('Tamanho da entrada')
    plt.ylabel('Tempo gasto')
    plt.title('Tempo do insertion sort')
    plt.show()
    
if __name__ == '__main__':
    main()


