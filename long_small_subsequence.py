arr=[10,22,9,33,21,50,41,60,50]

increasing=[1 for i in range(len(arr))]
decreasing=[1 for i in range(len(arr))]

def longest_increasing(increasing,arr):
    list1=[]
    for i in range(len(increasing)):
        for j in range(0,i):
            if arr[i]>arr[j] and increasing[i]<increasing[j]+1:
                increasing[i]=increasing[j]+1
                list1.append(arr[j])
    val=max(increasing)
    val1=[i for i in range(len(increasing)) if increasing[i]==val]
    list1.append(arr[val1[0]])
 #   print val1
 #   print arr
    print increasing
 #   print increasing[(len(arr)-1)]
 #   print list1

def longest_decreasing(decreasing,arr):
    for i in range(len(decreasing)):
        for j in range(0,i):
            if arr[i]<arr[j] and decreasing[i]<decreasing[j]+1:
                decreasing[i]=decreasing[j]+1
    print decreasing


longest_increasing(increasing,arr)
longest_decreasing(decreasing,arr)
max_val=max(increasing)
#print max_val
val1=[i for i in range(len(increasing)) if increasing[i]==max_val]
print val1
val=arr[val1[0]]
print val
decreasing_subsequence()




