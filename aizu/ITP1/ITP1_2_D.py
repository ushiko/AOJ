try:
     (W,H,x,y,r)  =  map(int,input().split())
except:
    exit

if ( (x - r) >= 0  and (W  >= (x +r)) and (y -r) >= 0 and (H >= (y +r))):
    print ("Yes")
else:
    print("No")

