import random
a=int(input())
b=int(input())
sum=0
c=[]
for i in range(a):
    stroka=[]
    for j in range(b):
        element=random.randint(0,50)
        sum=sum+element
        stroka.append(element)
    c.append(stroka)
print(c)
print(sum/(a*b))