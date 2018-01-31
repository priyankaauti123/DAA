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

def create_matrix1(e):
    dict1={}
    for i in range(e):
        v1=input("vertex1:=")
        v2=input("vertex2:=")
        w=input("weight:=")
        dict1[w]=(v1,v2)
    print dict1
    return dict1

def sort_according_to_weight(mat):
    for i in range(len(mat)):
        for j in range(0,i):
            if mat[i]<mat[j]:
                val=mat[i]
                mat[i]=mat[j]
                mat[j]=val
    return mat


#matrix=create_matrix(matrix,edge_no)
#print matrix
mat_dict={}
mat_dict=create_matrix1(edge_no)
print mat_dict
mat_dict=collections.OrderedDict(sorted(mat_dict.items()))
print mat_dict

kruskal(mat_dict)




