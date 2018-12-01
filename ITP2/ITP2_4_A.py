# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_4_A&lang=jp
# Reverse

from collections import deque
import sys
input = sys.stdin.readline

def main():
    n1 = int(input())
    l1 = list(map(int,input().split()))
    for i in range(int(input())):
        (a,b) = map(int,input().split())
        for ni in range((b-a)//2):
            l1[a+ni],l1[b-1-ni] = l1[b-1-ni],l1[a+ni]
    print (" ".join(map(str,l1)))


if __name__ == '__main__':
    main()