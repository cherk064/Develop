def print_all(*args,sep=" ",end="\n"):
    return sep.join(map(str,args))+end
    
print(print_all(1,2,3,4,sep="a",end="!"))


def map_list(func,*args):
    v=[]
    for i in args:
        v.append(list(map(func,i)))
    return v
a,b,c=[1,2,3,4],[23,-1],[None,[25]]
print(map_list(str,a,b,c))


def filter_list(func,*args):
    v=[]
    for i in args:
        v.append(list(filter(func,i)))
    return v
a,b,c=[1,2,3,4],[23,-1],[None,[25]]
numbers=lambda a: type (a) in (int,float)
print(filter_list(numbers,a,b,c))