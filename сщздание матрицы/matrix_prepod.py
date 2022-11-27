import random
n=4
m=4
a=[0]*n
for i in range(n):
    a[i]=[0]*m
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
print('*'*10)
for i in range(n):
    for j in range(m):
        a[i][j]=random.randint(1,5)
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
S1=0
S2=1

print('*'*10)
for i in range(n):
    a[i][S1], a[i][S2] = a[i][S2], a[i][S1]

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()