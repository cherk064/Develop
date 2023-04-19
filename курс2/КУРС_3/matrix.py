import random
class Matrix:
    def __init__(self,rows,colms):
        self.rows=rows
        self.colms=colms
        self.matrix=[[random.randint(-20,20) for i in range(colms)] for j in range(rows)]
    def print(self):
        print(self.matrix)
    def multiply(self,d):
        lam = lambda x: x * d       
        for i in range(self.rows):
            self.matrix[i] = list(map(lam, self.matrix[i]))
#            for t in range(self.colms):
 #               self.matrix[i][t]=self.matrix[i][t]*d


a=Matrix(6,5)
b=Matrix(7,2)
a.print()
b.print()
a.multiply(2)
a.print()

