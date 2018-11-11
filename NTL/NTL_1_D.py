import math

n = int(input())

soinsu = []

c = n
if (c % 2 == 0):
    while True:
        soinsu.append(2)
        c = c // 2
        if ( c % 2 != 0):
            break

len = int(math.sqrt(c)) + 1
for i  in range (3,len,2):
    while True:
        if ( c % i != 0):
            break
        soinsu.append(i)
        c = c // i
    if ( c == 1):
        break
if ( c != 1):
    soinsu.append(c)

d = n
for i in set(soinsu):
    d = d * (1-(1/i))
print (int(d))