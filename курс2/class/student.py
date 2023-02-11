class Student:
    def __init__(self,name="Ivan",groupNumber="10A",age="18"):
        self.name=name
        self.groupNumber=groupNumber
        self.age=age
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber
    def setGroupNumber(self,groupNumber):
        self.groupNumber = groupNumber
    def setNameAge(self,name,age):
        self.name = name
        self.age=age

student_1=Student()
student_2=Student("Vasya")
student_3=Student("Petya","15")
student_4=Student("Polina","16","9B")

students = [student_1, student_2, student_3, student_4]
for st in students:
    print(st.getAge())



print(student_1.getAge())
print(student_2.getName())
print(student_3.getGroupNumber())
student_4.setNameAge("Nastya","17")
student_4.setGroupNumber("10B")
print(student_4.getAge())
print(student_4.getName())
print(student_4.getGroupNumber())