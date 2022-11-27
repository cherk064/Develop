first=input("первый пират")
second=input("второй пират")
slovar={"ножницы":["бумага","ром"],
"бумага":["камень","пират"],
"камень":["ножницы","ром"],
"ром":["бумага","пират"],
"пират":["камень","ножницы"],
}
flag_nichia = True
first_spisok=slovar[first]
if first_spisok.__contains__(second):
    flag_nichia = False
    print("первый")
second_spisok=slovar[second]
if second_spisok.__contains__(first):
    flag_nichia = False    
    print("второй")
if flag_nichia:
    print("ничья")