#  http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_2_A&lang=jp
#   Parallel/Orthogonal : python3
#  2018.12.15 yonezawa

#from collections import deque
import sys
input = sys.stdin.readline
#import cProfile
from math import cos,sin,radians,sqrt

def main():

    for i in range(int(input())):
        (x1,y1,x2,y2,x3,y3,x4,y4) = map(int,input().split())

        inner = (x2-x1) * (x4-x3) + (y2-y1) * (y4-y3)
        cross = (x2-x1) * (y4-y3) - (x4-x3) * (y2-y1)               
        if inner == 0:
            print("1")
        elif cross == 0:
            print ("2")
        else:
            print("0")

    
if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()