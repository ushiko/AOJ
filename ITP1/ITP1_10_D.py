
from functools import reduce
import math


n = int(input())
l1  =  list(map(int,input().split()))
l2  =  list(map(int,input().split()))

sum1 = sum2 = sum3 = 0
max = 0
for i in range(0,n):
    sum1 += abs(l1[i] - l2[i])
    sum2 += pow(abs(l1[i] - l2[i]),2)
    sum3 += pow(abs(l1[i] - l2[i]),3)
    if ( max < abs(l1[i] - l2[i])):
        max = abs(l1[i] - l2[i])


print (sum1)
print (math.sqrt(sum2))
print (math.pow(sum3,1.0/3.0))
print (max*1.0)
