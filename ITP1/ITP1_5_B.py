while True:
    try:
        (H,W)  =  map(int,input().split())
    except:
        exit
    
    if (H == 0 and W == 0):
         break

    s1 = "#" * W
    
    if ( W >= 3 ):
        s2 = "#" + ("." * ( W -2 ) ) + "#"
    else:
        s2 = "#" * W

    print (s1)
    for i in range(0,H-2):
        print(s2)
    print(s1)
    print("")

    