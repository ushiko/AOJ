

try:
    (a,b)  =  map(int,input().split())
except:
    exit

print ('{} {}'.format(a//b,a%b), format(float(a/b),'.8f'))
