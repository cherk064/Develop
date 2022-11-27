a=[-8,0,6,4,2,1]
b=a
b.sort()
print(b)
c=len(a)
for i in range(c-1):
    for j in range(c-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
for v in range()

