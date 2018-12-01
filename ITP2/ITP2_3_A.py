# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_3_A&lang=jp
# Min-Max

from functools import reduce
from collections import deque
import sys
input = sys.stdin.readline


def main():
    l  = list ( map(int,input().split()))
    max = reduce(lambda a,b : a if a > b else b,l)
    min = reduce(lambda a,b : a if a < b else b,l)
    print (min,max)

if __name__ == '__main__':
    main()

    