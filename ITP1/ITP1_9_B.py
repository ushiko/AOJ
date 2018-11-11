
while True:
    w=str(input())
    if (w == "-"):
        break
    l = int(input())
    while (l > 0 ):
        n = int(input())
        l -= 1
        t1 = w[:n]
        t2 = w[n:]
        w = t2 + t1
    print (w)