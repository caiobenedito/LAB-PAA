import random
import timeit
import pickle
import matplotlib.pyplot as plt
import math

#----------------------- O(nlogn) -----------------------#

def maxCrossingSum(arr, l, m, h) : 
	sm = 0; left_sum = -10000
	for i in range(m, l-1, -1) : 
		sm = sm + arr[i] 
		if (sm > left_sum) : 
			left_sum = sm 
	sm = 0; right_sum = -1000
	for i in range(m + 1, h + 1) : 
		sm = sm + arr[i] 
		if (sm > right_sum) : 
			right_sum = sm 
	return left_sum + right_sum; 

def maxSubArraySum0(arr, l, h) : 
	if (l == h) : 
		return arr[l] 
	m = (l + h) // 2
	return max(maxSubArraySum0(arr, l, m), 
			maxSubArraySum0(arr, m+1, h), 
			maxCrossingSum(arr, l, m, h)) 
			
#----------------------- O(n) -----------------------#  

def maxSubArraySum2(a,size): 
	max_so_far = 0
	max_ending_here = 0	
	for i in range(0, size): 
		max_ending_here = max_ending_here + a[i] 
		if max_ending_here < 0: 
			max_ending_here = 0
		elif (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
	return max_so_far 

#----------------------- O(n2) -----------------------#  

def MaxSubarraySum(a,size):
  maximum = float('-inf')
  for i in range(0, size):
    current = 0
    for j in range(i, size):
       current += a[j]
       maximum = max(current, maximum)
  return maximum
#----------------------- O(n) recursive -----------------------#

def maxSubArraySum(a,low,high): 
    if(low == high):
        return [a[low],a[low],a[low],a[low]]
    else:
        mid=int(math.floor((low+high)/2))
        left=maxSubArraySum(a,low,mid)
        right=maxSubArraySum(a,mid+1,high)
        return compare(a,left,right)
    
def compare(a,l,r):
    totalSum=l[0]+r[0]
    maxPrefix=max(l[2],l[0]+r[2])
    maxSuffix=max(r[3],r[0]+l[3])
    maxSum=max(l[1],r[1],l[3]+r[2])
    return [totalSum,maxSum,maxPrefix,maxSuffix]


#-----------------------main-----------------------#  

def main():
    
    '''a = [-13, -3, -25, 20, -3, 16, -23, -12, -5, -22, -15, -4, -7]
    print "teta(n2) - Maximum contiguous sum is", MaxSubarraySum(a,len(a))    
    print "teta(nlogn) - Maximum contiguous sum is", maxSubArraySum0(a,0,len(a)-1)
    maxSum=maxSubArraySum(a,0,len(a)-1)
    print "teta(n) recursive - Maximum contiguous sum is ",maxSum[1]
    print "teta(n) - Maximum contiguous sum is", maxSubArraySum2(a,len(a))
    '''
    
    #print("This is a main function")
    #arr = randint(1, 10000^2)  
    arr=[]
    tamVector=9999
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
    for  i in range(1,21):
        arrAux=arr[1:i*tamVector+1+i]          
        x.append(len(arrAux))
        print len(arrAux)        
        start = timeit.default_timer()
        
        #stoogesort(arrAux,0,len(arrAux)-1)
        MaxSubarraySum(arrAux,len(arrAux))
        #maxSubArraySum0(arrAux,0,len(arrAux)-1)
        #maxSum=maxSubArraySum(arrAux,0,len(arrAux)-1)
        #maxSubArraySum2(arrAux,len(arrAux))
        
        stop = timeit.default_timer()
        time=stop-start
        stoogeSortTime.append(time)
        print 'MaxSubarraySum o(n2)'        
        #print 'MaxSubarraySum o(nlogn)'
        #print 'MaxSubarraySum o(n) recursive'
        #print 'MaxSubarraySum o(n) '
        
        print time
        
        
    
if __name__ == '__main__':
    main()


