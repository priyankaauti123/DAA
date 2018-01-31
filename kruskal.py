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

def create_matrix1(mat1,mat2,e):
    for i in range(e):
        v1=input("vertex1:=")
        v2=input("vertex2:=")
        w=input("weight:=")
        mat1.append((v1,v2))
        mat2.append(w)

#matrix=create_matrix(matrix,edge_no)
#print matrix
mat1=[]
mat2=[]

create_matrix1(mat1,mat2,edge_no)
print mat1,mat2





