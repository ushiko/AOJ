#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C&lang=jp
# List

from collections import deque
#import cProfile
#import time
import sys

input = sys.stdin.readline

def loop_proc():
    q1 = deque()
    q2  = deque()
    l2 = []
    cur = 0
    rflag = True
    n = int(input())
    cnt = 0

    while (cnt < n):
        cnt += 1
        if (rflag == True):
            l = list(map(int,input().split()))
        else:
            l = l2
        c = l[0]
        rflag =True
        #追加する場合
        if ( c == 0 ):
            d = l[1]
            #APPEND() & POP()は読み飛ばす
            if (cnt < n ):
                l2 = list(map(int,input().split()))
                if (l2[0] == 2 ):
                    cnt += 1
                    continue
                rflag =False
            q1.append(d)
        #カーソル移動の場合
        elif(c == 1):

            cur = l[1]
            if cur <  0 :
                for i in range(abs(cur)):
                    q1.append(q2.pop())
            else:
                for i in range(abs(cur)):
                    q2.append(q1.pop())
#            print (q1,q2)
        #要素削除の場合
        elif(c == 2):
            q1.pop()

    while len(q2) != 0 :
        print (q2.popleft())
    while len(q1) != 0 :
        print (q1.pop())

loop_proc()
#pr = cProfile.Profile()
#pr.runcall(loop_proc)
#pr.print_stats()