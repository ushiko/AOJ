import math

(x1,y1,x2,y2)=  map(float,input().split())
d = pow((x1-x2),2) + pow((y1-y2),2)
print (math.sqrt(d))
