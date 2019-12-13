import itertools

def main(): 
    cases=int(input())
    string=[]
    maxP=65
    
    dp=[]
    for i in range (0,maxP):
        new=[]
        for j in range(0,maxP):
            new.append(0)
        dp.append(new)
   
    for aux in range(cases):
        string=str(input()).replace('\r','')
        n=len(string)
        for i in range (0,n,1):
            for j in range(0,n,1):
                if((j+i)<n):
                    if(i == 0):
                        dp[j][j] = 1
                    elif(string[j] == string[j+i]):
                        dp[j][j+i] = dp[j][j+i-1]+dp[j+1][j+i]+1
                    else:
                        dp[j][j+i] = dp[j][j+i-1]+dp[j+1][j+i]-dp[j+1][j+i-1]
                        
        print( dp[0][n-1])
    
if __name__ == "__main__": 
    main()     