
from functools import reduce
import math

while True:
    n = int(input())
    if ( n == 0 ):
        break
    l  =  list(map(int,input().split()))
    mean = float(reduce(lambda a,b:a+b,l)) / (len(l))
    t = 0
    for i in l:
        t += pow((i - mean),2)
    bunsan = float(t) / len(l)
    print (math.sqrt(bunsan))
