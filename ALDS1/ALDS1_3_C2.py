# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C&lang=jp
#   Doubly Linked List : python3
#  2018.11.27 yonezawa


from collections import deque

import sys
input = sys.stdin.readline
import cProfile


def main():
    q = deque()
    n =  int(input())
    skipFlag = False

    while n > 0:
        if skipFlag == False:
            l = list(map(str,input().split()))
            if len(l) == 0:
                break
        skipFlag = False
        cmd = l[0]
        if ( cmd == 'insert'):
            d = int(l[1])
            if n <= 1:
                q.appendleft(d)
                n -= 1
                continue
            l = list(map(str,input().split()))
            if len(l) == 0:
                q.appendleft(d)
                break
            if (l[0] == 'deleteFirst' ):
                n -= 1
                continue
            elif (len(q) == 0 and l[0] == 'deleteLast'):
                n -= 1
                continue
            else:
                skipFlag = True
                q.appendleft(d)
        elif ( cmd == 'delete'):
            try:
                q.remove(int(l[1]))
            except:
                None
        elif ( cmd == 'deleteFirst'):
            q.popleft()
        else:
            q.pop()
        n -= 1

    print (*q)

if __name__ == '__main__':
   main()
#    pr = cProfile.Profile()
#    pr.runcall(main)
#    pr.print_stats()