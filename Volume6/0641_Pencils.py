
try:
     (N,a,b,c,d)  =  map(int,input().split())
except:
    exit
cnt = 0
min_cost = 1000000

while ( (cnt * a) < N + a):
    a_setnum = cnt 
    zan = N - (a_setnum * a) 
    if (zan < 0):
        zan = 0
    c_setnum = zan // c
    if ( zan % c != 0):
        c_setnum += 1
    cnt += 1
    cost =a_setnum * b + c_setnum *d
    if (min_cost > cost):
        min_cost = cost
print (min_cost)