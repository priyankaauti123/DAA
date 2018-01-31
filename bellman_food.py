import itertools as it

no=input("no of vertex:=")
ver1=[]
ver2=[]
weight=[]

def create_matrix(ver1,ver2,weight,n):
    for i in range(n):
        v1=input("vertex1:=")
        v2=input("vertex2:=")
        w=input("weight:=")
        ver1.append(v1)
        ver2.append(v2)
        weight.append(w)

def relax(v1,v2,w,d,p):
    if d[v2]>d[v1]+w:
        d[v2]=d[v1]+w
        p[v2]=v1
        #print d[v2],p[v2]

def bellman_food(d,p,ver1,ver2,weight):
    d[0]=0
    for i in range(len(d)):
        for j in range(len(ver1)):
            relax(ver1[j],ver2[j],weight[j],d,p)
    print d
    print p


create_matrix(ver1,ver2,weight,no)
print ver1,ver2,weight
d=[10000 for i in range(len(ver1))]
p=[-1 for i in range(len(ver1))]
bellman_food(d,p,ver1,ver2,weight)



