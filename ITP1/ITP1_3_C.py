

while True:
    try:
        (a,b)  =  map(int,input().split())
    except:
     exit
    if ( a == 0 and b == 0):
        break
    elif ( a < b):
        print(a,b)
    else:
        print (b,a)
