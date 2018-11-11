w = str(input())
n = int(input())
while ( n > 0 ):
    n = n -1
    l  =  list(map(str,input().split()))
    if (l[0] == "print" ):
        print (w[int(l[1]):int(l[2])+1])
    elif(l[0] == "replace"):
        p1 = int(l[1])
        p2 = int(l[2])
        w = w[:p1] + l[3] + w[p2+1:]
    elif(l[0] == "reverse"):
        p1 = int(l[1])
        p2 = int(l[2])
        t1 = w[:p1]
        t2 = w[p1:p2+1]
        t3 = w[p2+1:]
        w = t1 + t2[::-1] + t3
