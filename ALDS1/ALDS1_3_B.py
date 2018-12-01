# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B&lang=jp
#  Queue : python3
#  2018.11.26 yonezawa

from collections import deque
import sys
input = sys.stdin.readline

def calc(t,q):
    tq = deque()
    counter = 0
    while len(q) > 0:
#        print ("count",counter,q)
        (i1,i2) = q.popleft()
        if (i2 > t):
            i2 = i2 - t
            q.append((i1,i2)) 
            counter = counter + t
        else:
            i2 = counter + i2
            tq.append((i1,i2))
            counter = i2
    return tq
def main():
    (n,t) = map(int,input().split())
    q = deque()
    for i in range(n):
        (a,b) = map(str,input().split())
        q.append((a,int(b)))
    for a,b in calc(t,q):
        print (a,b)
if __name__ == '__main__':
    main()