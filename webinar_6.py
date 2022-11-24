def Cesaer(b,key):
    result=""
    for i in b:
        ind=a.index(i)
        newind=ind+key
        c=a[newind]
        result=result+c
    return result

a=["a","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
b=input()
key=int(input())
print(Cesaer(b,key))


