def greet(a, *args):
    name=" and ".join((a,)+args)
    return f"Hello,{name}!"
print(greet("Timur"))
print(greet("Timur","Roma"))