import random
n=4
m=4
a=[0]*n
for i in range(n):
    a[i]=[0]*m
print(a)
for i in range(n):
    for j in range(m):
        a[i][j]=random.randint(1,5)
print(a)