def ip_check(ip):
    a=ip.split(".")
    if len(a)<4:
        return False
    lam = lambda x: True if x.isnumeric() and int(x)<=255 and int(x)>=0 else False
    return all(map(lam,a))
print(ip_check("10.0.1.1"))
print(ip_check("10.0.1.a"))
print(ip_check("10.0.1.260"))