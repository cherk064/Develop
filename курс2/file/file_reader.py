columns=('id', 'name', 'lastname', 'age', 'height', 'weight')
data = [
    (1, 'Ivan', 'Ivanov', 14, 160, 50),
    (2, 'Sasha', 'Sidorov', 15, 210, 40),
    (3, 'Masha', 'Poradina', 30, 178, 70),
    (4, 'Timur', 'Korolev', 44, 160, 120),
    
]

def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append((line[0], line[1], line[2], line[3], line[4], str(line[5]).replace("\n","")))
    return columns, data

def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(columns)+'\n')
        for line in data:
            line=[str(i) for i in line]
            file.write(','.join(line)+'\n')

def print_from_file():
    a=read_from_file("D:\\Develop\\курс2\\file\\data.csv")
    print(" ".join(a[0]))
    datalist = a[1]
    row_count = len(datalist)
    for i in range(row_count):
        row = datalist[i]
        print(" ".join(row))

polz=input("введите имя и фамилию,возвраст,рост,вес").split(" ")
data.append(polz)
write_to_file("D:\\Develop\\курс2\\file\\data.csv")
print_from_file()
