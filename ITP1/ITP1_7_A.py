

while True:
    (a,b,c)  =  map(int,input().split())
    if ( a == b == c == -1 ):
        break
    if ( a == -1 or b == -1):
        print ("F")
        continue
    if ( a + b >= 80):
        print ("A")
        continue
    elif(a + b >= 65 ):
        print ("B")
        continue
    elif(a + b >= 50 ):
        print ("C")
        continue
    elif(a + b >= 30 ):
        if ( c >= 50):
            print ("C")
        else:
            print ("D")
        continue
    print("F")


