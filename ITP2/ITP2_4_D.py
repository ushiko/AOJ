# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_4_D&lang=jp
# Unique

from collections import deque
import sys
input = sys.stdin.readline

def main():
    n1 = int(input())
    l1 = list(map(int,input().split()))
    print(*sorted(list(set(l1))))
if __name__ == '__main__':
    main()