# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_B&lang=jp
#  Set: Delete: python3
#  2018.12.02 yonezawa

import sys
input = sys.stdin.readline
import collections

def main():
    tl = {}
    for i in range(int(input())):
        l = list(map(int,input().split()))

        #insert
        cmd = l[0]
        if cmd == 0:
            tl[l[1]] = 1
            print (len(tl))
        #find
        elif cmd == 1:
            c = 1 if l[1] in tl else 0
            print (c)
        #delete
        elif cmd == 2:
            d = l[1]
            try:
                tl.pop(d)
            except KeyError:
                None
if __name__ == '__main__':
    #main()
    pr = cProfile.Profile()
    pr.runcall(main)
    pr.print_stats()
