

while True:
    try:
     (a,b,c)  =  map(str,input().split())
    except:
     exit
    if ( b == "?"):
        break

    a = int(a)
    c = int(c)

    if ( b == "+"):
        print (a + c)
    elif (b == "-"):
        print (a - c)
    elif (b == "*"):
        print (a * c)
    elif (b == "/"):
        print (a // c)
