s1=s2=0
n = int(input())
while ( n > 0 ):
    n = n -1
    (a,b)  =  map(str,input().split())

    if (a > b):
        s1 += 3
    elif (b > a):
        s2 += 3
    else:
        s1 += 1
        s2 += 1
print (s1,s2)