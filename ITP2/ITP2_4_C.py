# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_4_C&lang=jp
# Swap

from collections import deque
import sys
input = sys.stdin.readline

def main():
    n1 = int(input())
    l1 = list(map(int,input().split()))
    for i in range(int(input())):
        (b,e,t) = map(int,input().split())
        for k in range(e-b):
            l1[k+b],l1[t+k] = l1[t+k] ,l1[k+b]
    print (" ".join(map(str,l1)))

if __name__ == '__main__':
    main()