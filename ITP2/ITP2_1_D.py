#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_D&lang=jp
# Vector II
 
from collections import deque
import sys
input = sys.stdin.readline
 
def loop_proc():
    (n1,n2) = map(int,input().split())
    wl =[]
    for i in range(n1):
        wl.append(deque())
    for i in range(n2):
        l = list(map(int,input().split()))  
        if (l[0] == 0 ):
            wl[l[1]].append(l[2])
        elif (l[0] == 1 ):
            if ( len(wl[l[1]]) == 0 ):
                print ("")
            else:
                print (" ".join(map(str,wl[l[1]])))
        elif (l[0] == 2 ):
            wl[l[1]] = deque()
  
 
loop_proc()