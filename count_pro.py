




def count_coin(n):
    sol=0
    if n==0:
        return 0
    sol1=1+count_coin(n-1)
    sol=sol1
    if n>=29:
        sol2=1+count_coin(n-29)
        sol=min(sol,sol2)
    if n>=50:
        sol3=1+count_coin(n-50)
        sol=min(sol,sol3)
    return sol


no=count_coin(59)
print no
