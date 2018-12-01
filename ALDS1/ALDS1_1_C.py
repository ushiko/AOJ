# Prime Numbers
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C&lang=jp

import math
def isPrime(c):
    if (c == 2 ):
        return True
    if (c % 2 == 0 ):
        return False
    len = int(math.sqrt(c)) + 1
    for i  in range (3,len+1,2):
        if ( c % i == 0):
            return False  
    return True

cnt = 0
n = int(input())
while ( n > 0):
    n = n -1
    s = int(input())
    if ( isPrime(s) == True ):
        cnt += 1
print (cnt)