glasy=["а","о","ё","е","э","ю","я","и","у","ы"]

a=input("введите предложение")
b=a.lower()
chet=0
for i in a:
    if glasy.__contains__(i):
        chet+=1
print(chet)