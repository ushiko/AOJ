#  http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_C&lang=jp
#  Koch Curve : python3
#  2018.12.09 yonezawa




#from collections import deque
import sys
input = sys.stdin.readline
import cProfile
from math import cos,sin,radians

def koch(n,st,ed):
    if (n == 0 ):
        print ('{:.8f} {:.8f}'.format(*ed))
        return
    s1 = st
    s5 = ed
    (x1,y1) = st
    (x5,y5) = ed

    x2 = x1 + (x5 - x1) / 3.0
    y2 = y1 + (y5 - y1)  / 3.0
    s2 = (x2,y2)

    x4 = x1 + ((x5 -x1 ) / 3.0 ) * 2
    y4 = y1 + ((y5 - y1) / 3.0 ) * 2
    s4 = (x4,y4)

    x3 = (x4-x2) * cos(radians(60)) - (y4-y2 ) * sin(radians(60)) + x2
    y3 = (x4-x2) * sin(radians(60)) + (y4-y2 ) * cos(radians(60)) + y2
    s3 = (x3,y3)

    t.add(s1)
    t.add(s2)
    t.add(s3)
    t.add(s4)
    t.add(s5)
    #print ("n=",n,*s1)
    koch (n-1,s1,s2)
    #print ("n=",n,*s2)
    koch (n-1,s2,s3)
    #print ("n=",n,*s3)
    koch (n-1,s3,s4)
    #print ("n=",n,*s4)
    koch (n-1,s4,s5)
    #print ("n=",n,*s5)

def main():
    n = int(input())
    print ('{:.8f} {:.8f}'.format(0,0))
    koch(n,(0,0),(100,0))

if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()