from math import acos,cos,degrees,radians,ceil,floor
import re

A = 90
a = int(input())
b = int(input())
c = (a**2+b**2-2*a*b*cos(radians(A)))**.5
c2 = c/2
B = degrees(acos((c**2+b**2-a**2)/(2*c*b)))
m = (c2**2+b**2-2*c2*b*cos(radians(B)))**.5
M = str(degrees(acos((m**2+b**2-c2**2)/(2*m*b))))
if int(re.search(r'\.[0-9]',M).group()[1])>=5:
    M=ceil(float(M))
else:
    M = floor(float(M))
print(str(M)+chr(176))
