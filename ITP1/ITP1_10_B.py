import math

(a,b,c)=  map(int,input().split())

h = math.sin(math.radians(c)) * b
L = a + b +math.sqrt(a*a+b*b-(2*a*b*math.cos(math.radians(c))))
S = h * a / 2
print (S)
print (L)
print (h)

