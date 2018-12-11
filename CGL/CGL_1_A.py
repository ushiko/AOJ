#  http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_1_A&lang=jp
#  Projection : python3
#  2018.12.10 yonezawa

#from collections import deque
import sys
input = sys.stdin.readline
#import cProfile
from math import cos,sin,radians,sqrt

def Projection(p1,p2):
    (x1,y1,x2,y2) = p1
    if (x1*x1+y1*y1 > x2*x2 + y2*y2):
        (x1,y1,x2,y2) = (x2,y2,x1,y1)
    (x3,y3) = p2

    tx = x2 -x1
    ty = y2 -y1
    l = sqrt(tx*tx+ty*ty)

    nx = tx / l
    ny = ty / l
    pl = nx * (x3 - x1)  + ny * (y3 - y1)
    return (nx * pl + x1, ny * pl + y1 )


def main():
    (x1,y1,x2,y2) = map(int,input().split())
    for i in range(int(input())):
        (x3,y3) = map(int,input().split())
        print('{:.10f} {:.10f}'.format(*Projection((x1,y1,x2,y2),(x3,y3))))

    
if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()