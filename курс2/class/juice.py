class Juice:
    counter = 0
    def __init__(self,a):
        
        Juice.counter=Juice.counter + 1
        self.dobavka=a
    
    def my_juice(self):
        if self.dobavka=="":
            print("добавки нет")
        else:
            print("добавка",self.dobavka)

juice_1 = Juice("")
print(juice_1.counter)
print(juice_1.dobavka)
juice_2=Juice("вода")
print(juice_2.counter)
print(juice_1.counter)
print(Juice.counter)
print(juice_2.dobavka)

