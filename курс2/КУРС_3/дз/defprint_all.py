def print_all(*args,sep=" ",end="\n"):
    return sep.join(map(str,args))+end
    
print(print_all(1,2,3,4,sep="a",end="!"))