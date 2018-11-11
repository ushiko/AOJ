def exgcd(n1,n2): 
    x1,y1,m1 = (1,0,n1)
    x2,y2,m2 = (0,1,n2)
    while( n2 != 0):
        t = n1 // n2
        if (m1 >= m2):
            x1 -=  (x2 * t)
            y1 -=  (y2 * t)
            m1 -=  (m2 * t)
        else:
            x2 -= (x1 * t)
            y2 -= (y1 * t)
            m2 -= (m1 * t)
        i = n2
        n2 = n1 % n2
        n1 = i
    if (m1 == 1):return x1,y1
    return x2,y2

(m,n)  =  map(int,input().split())
(a1,b1) =  exgcd(m,n)
(a2,b2) =  exgcd(n,m)


if (abs(a1)+abs(b1) < abs(a2) + abs(b2)):
    print(a1,b1)
elif (abs(a1)+abs(b1) > abs(a2) + abs(b2)):
    print(b2,a2)
else:
    if (b1 >= a1):
        print(a1,b1)
    else:
        print(b2,a2)
