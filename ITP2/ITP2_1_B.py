# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_B&lang=jp
# Deque

from collections import deque

q = deque()
for i in range(0,int(input())):
    l = list(map(str,input().split()))
    c = int(l[0])

    if ( c == 0 ):
        d = int(l[1])
        if (d == 0):
            q.appendleft(l[2])
        elif (d == 1):
            q.append(l[2])
    elif(c == 1):
        d = int(l[1])
        print (q[d])
    elif(c == 2):
        d = int(l[1])
        if (d == 0):
            q.popleft()
        elif (d == 1):
            q.pop()