from roman import *

t = ['IV', 'LVIII', 'MCMXCIV', 'XCIX', 'LXXX', 'LXXX']
print(t)
for i in t:
    print(i, '->' ,roman_to_int(i))

a=[4, 58, 1994, 26, 99, 69]
for i in a:
    print(i, '->',int_to_roman(i))