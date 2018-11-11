(m,n)  =  map(int,input().split())

bi = str(format(n,"b"))
bi = bi[::-1]

c = 1
d = 1000000007

for i in bi:
    if ( i == "1"):
        c = ( c * m ) % d
    m = (m * m) %d
print (c)

