
def map_list(func,*args):
    v=[]
    for i in args:
        v.append(list(map(func,i)))
    return v
a,b,c=[1,2,3,4],[23,-1],[None,[25]]
print(map_list(str,a,b,c))