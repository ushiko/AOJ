import math
try:
    n = int(input())
except:
    exit

max_len = n 
work = [1 for i in range(0,max_len+1)]
prime = [2,3]
soinsu = []
max_prime = n // 2 

for i in range(3,max_prime+1,2):

    if ( i % 2 == 0 or i % 3 == 0 ):
        continue
    maxp = int(math.sqrt(i)) + 1
    for j in prime:
        if ( i % j == 0 ):
            break
        if ( maxp < j):
            prime.append(i)
            break
    else:
        prime.append(i)
prime.append(i)
print(prime)
t = n
while (t > 1):
    for i in prime:
        if (t % i == 0 ):   
            t = t // i
            soinsu.append(i)
soinsu.sort()
print (n,":",end ="",sep ="")
for i in soinsu:
    print (" ",i, end ="",sep="")
