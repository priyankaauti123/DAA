weight=[10,20,30]
value=[60,100,120]
capacity=50

def average(w,v):
    avg=[]
    for i in range(len(w)):
        avg.append(v[i]/w[i])
    return avg

def knapsak(avg,capacity,w,v):
    val1=0
    val2=0
    list1=[]
    for i in range(len(avg)):
        val=0
        val=w[i]
        if capacity==0:
            print list1
            return list1
        else:
            if capacity>val:
                val1+=val
                capacity-=val
                val2+=v[i]
                list1.append(v[i])
            else:
                #print (capacity*v[i])/w[i]
                val1+=capacity
                val2+=(v[i]*capacity)/w[i]
                list1.append(v[i]*capacity//w[i])
                capacity-=capacity
                print capacity
    print val1
    print val2
    return list1



avg=average(weight,value)
print avg

list1=knapsak(avg,capacity,weight,value)
print list1
print sum(list1)



