class Juice:
    def __init__(self,a):
        self.dobavka=a
    
    def my_juice(self):
        if self.dobavka=="":
            print("добавки нет")
        else:
            print("добавка",self.dobavka)

juice_1 = Juice("")
juice_2=Juice("вода")

juice_1.my_juice()
juice_2.my_juice()
