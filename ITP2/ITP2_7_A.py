# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_A&lang=jp
#  Set: Search: python3
#  2018.12.02 yonezawa

import sys
input = sys.stdin.readline
import collections

def main():
    tl = {}
    for i in range(int(input())):
        l = list(map(int,input().split()))

        if l[0] == 0:
            tl[l[1]] = 1
            print (len(tl))
        else:
            c = 1 if l[1] in tl else 0
            print (c)
            
if __name__ == '__main__':
    main()