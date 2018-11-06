while True:
    try:
        (H,W)  =  map(int,input().split())
    except:
        exit
    
    if (H == 0 and W == 0):

         break
    s = "#." * 151

    for i in range(0,H):
        print(s[i%2:W+i%2])
    print("")

    