# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_3_D&lang=jp
# Lexicographical Comparison

from functools import reduce
from collections import deque
import sys
input = sys.stdin.readline


def main():
    n1 = int(input())
    l1  = "".join(map(str,input().split()))
    n2 = int(input())
    l2  = "".join(map(str,input().split()))
    if (l1 >= l2):
        print (0)
    else:
        print(1)

if __name__ == '__main__':
    main()