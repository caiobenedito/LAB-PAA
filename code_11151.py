import itertools

def main(): 
    cases=int(input())
    string=[]
    maxP=1001
    
    DP=[]
    for i in range (0,maxP):
        new=[]
        for j in range(0,maxP):
            new.append(0)
        DP.append(new)
   
    for aux in range(cases):
        string=str(input())
        n=len(string)
        for i in range (0,n,1):
            for j in range(0,n,1):
                if((j+i)<n):
                    if(string[j] == string[i+j]):
                        DP[j][j+i] = DP[j+1][j+i-1] + (i == 0 and 1 or 2)
                    else:
                        DP[j][j+i] = max(DP[j+1][j+i], DP[j][j+i-1])
                    
        print( DP[0][n-1])
    
if __name__ == "__main__": 
    main()     