# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_3_C&lang=jp
# Count

from functools import reduce
from collections import deque
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    l  = list ( map(int,input().split()))

    for i in range(int(input())):
        (n1,n2,a) = map(int,input().split())    
        count = len(list(filter(lambda x : x == a,l[n1:n2])))
        print (count)

if __name__ == '__main__':
    main()