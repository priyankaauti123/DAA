import collections




vertex_no=input("no of vertices:=")
edge_no=input("no of edges:=")
matrix=[[0 for i in range(vertex_no)]for j in range(vertex_no)]


def add_edge(v1,v2,w,matrix):
    matrix[v1][v2]=w
    matrix[v2][v1]=w
    return matrix

def create_matrix(matrix,e):
    for i in range(e):
        v1=input("vertex1:=")
        v2=input("vertex2:=")
        val=input("weight:=")
        matrix=add_edge(v1,v2,val,matrix)
    return matrix

def find_min_weight(rem_vertex,matrix,min_ver,min_span_tree):
    min_val=[]
    val1=[]
    val2=[]
    for i in range(len(min_ver)):
        for j in range(len(rem_vertex)):
            if matrix[min_ver[i]][rem_vertex[j]]!=0:
                min_val.append(matrix[min_ver[i]][rem_vertex[j]])
                val1.append(min_ver[i])
                val2.append(rem_vertex[j])
    if min_val!=[]:
        min_val1=min(min_val)
        for i in range(len(min_val)):
            if min_val1==min_val[i]:
                val_2=val2[i]
                val_1=val1[i]
                matrix[val_1][val_2]=0
                min_span_tree[val_1][val_2]=min_val1
                rem_vertex=list(filter(lambda x:x!=val_2,rem_vertex))
                #print rem_vertex
                min_ver.append(val_2)
                return (min_val1)
    else:
        return 0


def minimum_spanning_tree(matrix):
    min_span_tree=[[0 for i in range(len(matrix))]for j in range(len(matrix))]
    min_weight=[]
    rem_ver=[]
    min_ver=[]
    min_ver.append(0)
    rem_ver=[i for i in range(1,len(matrix))]
    for i in range(len(matrix)):
        min_val=find_min_weight(rem_ver,matrix,min_ver,min_span_tree)
        print min_val,rem_ver,min_ver
        if min_val!=0:
            min_weight.append(min_val)
    print min_val,rem_ver,min_ver
    print matrix
    print min_span_tree


matrix=create_matrix(matrix,edge_no)
print matrix

minimum_spanning_tree(matrix)
#find_min_weight(matrix)

