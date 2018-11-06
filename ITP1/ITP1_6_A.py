try:
     (n)  =  int(input())
except:
    exit
try:
    l =  list(map(int,input().split()))
except:
    exit

l.reverse()
for i in l:
    print(i,end="")
    if ( n != 1 ):
        print (" ",end="")
    n = n -1
print ("")
