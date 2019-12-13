import itertools

def main(): 
    cases=int(input())
    string=[]
    max=1011
    
    f=[]
    for i in range (0,max):
        new=[]
        for j in range(0,max):
            new.append(0)
        f.append(new)
   
    for aux in range(cases):
        string=str(input()).replace('\r','')
        j=1
        n=len(string)
        i=0
        for len_aux in range(2,n+1,1):
            for j,i in zip(range(len_aux-1,n+1,1), range(0,n-(len_aux-1)+1,1)) :
                    if(j<n):     
                        f[i][j] = min(f[i + 1][j] + 1, f[i][j - 1] + 1)
                        if(string[i]==string[j]):
                            f[i][j] = min(f[i][j], f[i + 1][j - 1])
                        else:
                            f[i][j] = min(f[i][j], f[i + 1][j - 1] + 1)
                
        print("Case "+str(aux+1)+": "+str(f[0][n-1]))
    
if __name__ == "__main__": 
    main()     