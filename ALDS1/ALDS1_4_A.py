# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_A&lang=jp
#  Linear Search : python3
#  2018.12.08 yonezawa


#from collections import deque
import sys
input = sys.stdin.readline
#import cProfile

def main():
    n1 = int(input())
    s1 = set(map(int,input().split()))
    n2 = int(input())
    s2 = set(map(int,input().split()))
    print (len(s1 & s2))

if __name__ == '__main__':
   main()
#    pr = cProfile.Profile()
#    pr.runcall(main)
#    pr.print_stats()