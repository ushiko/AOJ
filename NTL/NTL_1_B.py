try:
    (m,n)  =  map(int,input().split())
except:
    exit

r = pow(m,n) %  1000000007
print (r)


