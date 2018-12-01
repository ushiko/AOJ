# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_2_C&lang=jp
# Priority Queue

from collections import deque
import sys
input = sys.stdin.readline
import heapq

def loop_proc():
    (n1,n2) = map(int,input().split())
    wl =[]
    for i in range(n1):
        wl.append(list())
    for i in range(n2):
        l = list(map(int,input().split()))  
        if (l[0] == 0 ):
            n = l[1]
            d = l[2]
            heapq.heappush(wl[n],-1 * d)
        elif (l[0] == 1 ):
            if ( len(wl[l[1]]) != 0 ):
                tl = wl[l[1]]
                a = heapq.heappop(tl) 
                heapq.heappush(tl,a) 
                print (int(a) * -1 )
        elif (l[0] == 2 ):
            if ( len(wl[l[1]]) != 0 ):
                tl = wl[l[1]]
                heapq.heappop(tl)  


if __name__ == '__main__':
    loop_proc()
#   import cProfile
#   pr = cProfile.Profile()
#   pr.runcall(loop_proc)
#   pr.print_stats()