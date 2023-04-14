a=int(input())
b=int(input())
c=int(input())
def solve(a,b,c):
    diskr=b**2-4*a*b
    if diskr>0:
        x1=(-b+(diskr*0.5))//2*a
        x2=(-b-(diskr*0.5))//2*a
        print(x1,x2)
    else:
        print("нет корней")
