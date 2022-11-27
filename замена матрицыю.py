import random

a=[]

n=int(input('n? '))
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(random.randint(1,99))
    a.append(temp)
t=int(input())
f=int(input())
print(a)
for v in range(n-1):
    a[v][t], a[v][f]=a[v][f], a[v][t]
print(a)