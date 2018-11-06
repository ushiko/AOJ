

try:
    n  =  int(input())
except:
    exit

    
try:
    l =  input().split()
except:
    exit

l_n = [int(i) for i in l]

print (min(l_n),max(l_n),sum(l_n))


