def round_up(x,y):
    x_float=float(x)
    y_float=float(y)
    if (x_float/y_float)==int((x_float/y_float)):
        return (x//y)
    else:
        return (x//y)+1

def logarithm(x):
    i=1;
    if(x==1):
        return 0
    while(True):
        if(2**i<=x) and (2**(i+1)>x):
            return i
        else:
            i=i+1

def binary_sum(x,y):
    result=[]*len(x)
    for i in range(0,len(x)):
        result.append(int(x[i] or y[i]))
    return result

def Num(x):
    number=0
    for i in range(0, len(x)):
        number=number+x[i]*(2**(len(x)-1-i))
    return number

def binary_sum2D(z,b):
    result=[[]]*len(z)
    for i in range(0, len(z)):
        result[i]=binary_sum(z[i],b[i])
    return result
        
        
        

def four_russians(A,B,n):
    m=logarithm(n)
    C=[]
    ZeroRow=[0]*n
    for i in range(n):
        C.append(ZeroRow)
    final=round_up(n,m)
    for i in range(1,final+1):
        EndOfBi = i*m-1
        rs=[[]]*(2**m)
        ZeroRow=[0]*n
        rs[0]=ZeroRow
        bp=1
        k=0
        for j in range(1,2**m):
            if((i*m-k-1)<n):
                rs[j]=binary_sum(B[EndOfBi-k],rs[j-2**k])
            else:
                 rs[j]=binary_sum([0]*n,rs[j-2**k])
            if (bp==1):
                bp=j+1
                k=k+1
            else:
                bp=bp-1
                
        Ci= [[]]*n
        StartColumn=(i-1)*m
        EndColumn=i*m-1
        if(i*m-1)<n:
            Ai=[k[StartColumn:EndColumn+1]for k in A]
        else:
            Ai=[k[StartColumn:EndColumn+1]for k in A]
            Ai=[k+[0]*(i*m-n) for k in Ai]
            
        for j in range(0,n):
            Ci[j]=rs[Num(Ai[j])]
        C=binary_sum2D(C, Ci)
        
    return C  
            
        
        
    
    


import sys

if (len(sys.argv) == 2):
    print()
    print(" To metavatiko kleisimo tou grafou einai:")
    maxVertice=-1
    with open(str(sys.argv[1]), "r") as first:
        for line in first:
            currentLine=line.split()
            currentLine=list(map(int,currentLine))
            if(currentLine[0]>maxVertice):
                maxVertice=currentLine[0]
            if(currentLine[1]>maxVertice):
               maxVertice=currentLine[1]
               
        n=maxVertice+1
        adjacency=[]
        for i in range(n):
            ZeroRow=[0]*n
            ZeroRow[i]=1
            adjacency.append(ZeroRow)
            
    with open(str(sys.argv[1]), "r") as first2:   
        for line2 in first2:
            currentLine2=line2.split()
            currentLine2=list(map(int,currentLine2))
            adjacency[currentLine2[0]][currentLine2[1]]=1

    temp=adjacency
    for i in range(0,n):
        adjacency= four_russians(temp,adjacency,n)


    for z in range(0,n) :
        for i in range(0,n):
            if(adjacency[z][i]==1):
                    output=' ' + str(z) +' ' + str(i)
                    print(output)

        
        
elif (len(sys.argv) == 3):
    print()
    print("four russians")
    print()
    
    A = []
    B = []
    with open(str(sys.argv[1]), "r") as first:
        for line in first:
             line = line.rstrip('\n')   
             currentline = line.split(",")
             currentline = list(map(int, currentline))
             A.append(currentline)
             
    with open(str(sys.argv[2]), "r") as second:
        for line in second:
             line = line.rstrip('\n')   
             currentline = line.split(",")
             currentline = list(map(int, currentline))
             B.append(currentline)
    n=len(A)         
    answer=four_russians(A,B,n)
    print("The result of A*B is:")
    print()

    for row in answer:
        y=str(0)
        y=','.join([str(x)for x in row])
        print(y)
        print
    



    
