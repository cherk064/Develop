a=[9,56,99,67,5]
b=len(a)
c=a[0]
d=0
for index in range(b):
    if a[index]>c:
        c=a[index]
        d=index

print(c,d+1)

