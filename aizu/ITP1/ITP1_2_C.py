try:
    (a,b,c)  =  map(int,input().split())
except:
    exit

n = [a,b,c]
n.sort()
print ('{0[0]} {0[1]} {0[2]}'.format(n))