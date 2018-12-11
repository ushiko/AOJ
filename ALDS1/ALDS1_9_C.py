# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C&lang=jp
# Priority Queue
# 2018.12.09 yonezawa

#from collections import deque
import sys
input = sys.stdin.readline
import heapq
#import cProfile

def main():
    tl = []
    while True:
        l  = list(map(str,input().split()))
        if l[0] == "end":
            break
        if l[0] == "insert":
            heapq.heappush(tl,int(l[1]) * -1)
        if l[0] == "extract":
            a = heapq.heappop(tl) * -1 
            print (a)

if __name__ == '__main__':
    main()
   #pr = cProfile.Profile()
   #pr.runcall(main)
   #pr.print_stats()