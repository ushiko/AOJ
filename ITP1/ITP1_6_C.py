
n =  int(input())


tatemono = [0] * 4 * 3 *10
while ( n > 0 ):
    (b,f,r,v)  =  map(int,input().split())
    tatemono[(b-1)*30 + (f-1)*10 + r-1] += v
    n = n -1


for  i in range (0,4):
    for  i2 in range (0,3):
        for  i3 in range (0,10):
            print (' {}'.format(tatemono[i3 + i*30 + i2*10]),end="")
        else:
            print("")
    if ( i != 3 ):
        print ("####################")

