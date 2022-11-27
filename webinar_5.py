a=[]
n=int(input('n? '))
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(int(input()))
    a.append(temp)
print(a)