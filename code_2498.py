import itertools

def main(): 
    dp=[]
    for i in range (0,2):
        new=[]
        for j in range(0,100000):
            new.append(0)
        dp.append(new)
        
    cont=1
    [n,c]=input().replace('\r','').split()
    n=int(n)
    c=int(c)
    while((n and c)!=0):
        v=[]
        w=[]
        w.append(0)
        v.append(0)
        for i in range(1,n+1,1):
            [x,y]=input().replace('\r','').split()
            w.append(int(x))
            v.append(int(y))
               
        for i in range(0,c+1,1):
            dp[0][i] = 0
        dp[1][0] = 0
        
        for i in range(1,n+1,1):
            for j in range(1,c+1,1):
                if(w[i]  <= j):
                    dp[i%2][j] = max(dp[(i-1)%2][j],dp[(i-1)%2][j-w[i]]+v[i]);
                else:
                    dp[i%2][j] = dp[(i-1)%2][j];
        
        print ("Caso "+str(cont)+": "+str(dp[n%2][c]))
        [n,c]=input().replace('\r','').split()
        n=int(n)
        c=int(c)
if __name__ == "__main__": 
    main()     