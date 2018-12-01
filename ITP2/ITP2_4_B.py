# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_4_B&lang=jp
# Rotate

from collections import deque
import sys
input = sys.stdin.readline

def main():
    n1 = int(input())
    l1 = list(map(int,input().split()))
    l2 = []
    for i in range(int(input())):
        (b,m,e) = map(int,input().split())   
        for k in range(b):
            l2.append(l1[k])
        for k in range(m,e):
            l2.append (l1[k]) 
        for k in range(b,m):
            l2.append(l1[k])
        for k in range(e,len(l1)):
            l2.append(l1[k])
        l1 = l2
        l2 = []
    print (" ".join(map(str,l1)))


if __name__ == '__main__':
    main()