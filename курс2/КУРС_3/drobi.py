class Fraction:
    def __init__(self,top,bot):
        self.top=top
        self.bot=bot
    def __str__(self):
       return "{0}/{1}".format(self.top,self.bot)
    def decimal(self):
        return self.top/self.bot
    def nod(self):
        nod=0
        if self.top>self.bot:
    


a=Fraction(5,6)
print (a)
print (a.decimal())
    