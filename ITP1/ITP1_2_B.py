
try:
     (a,b)  =  map(int,input().split())
except:
    exit

if (a > b):
    print("a > b")
elif (a == b):
    print ("a == b")
else:
    print("a < b")