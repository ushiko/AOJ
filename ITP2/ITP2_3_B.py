# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_3_B&lang=jp
# Min-Max Element

from functools import reduce
from collections import deque
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    l  = list ( map(int,input().split()))

    for i in range(int(input())):
        (a,n1,n2) = map(int,input().split()) 
        if (a == 0):   
            min = reduce(lambda a,b : a if a < b else b,l[n1:n2])
            print (min)
        elif (a==1):
            max = reduce(lambda a,b : a if a > b else b,l[n1:n2])
            print (max)

if __name__ == '__main__':
    main()