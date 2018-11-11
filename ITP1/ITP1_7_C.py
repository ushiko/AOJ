from functools import reduce

(r,c)=  map(int,input().split())

l = []
for i in range(0,r):
    t = list(map(int,input().split()))
    t.append(reduce(lambda a,b:a+b,t))
    l.append(t)

l2 = []
for i in list(map(list, zip(*l))):
    l2.append(reduce(lambda a,b:a+b,i))
l.append(l2)

for i in range(0,r+1):
    print (' '.join(map(str,l[i]))) 
