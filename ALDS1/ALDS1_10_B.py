# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_B&lang=jp
#  Matrix Chain Multiplication : python3
#  2018.12.03 yonezawa

from collections import deque
import sys
input = sys.stdin.readline

def main():
    nmax = 1000000
    n = int(input())
    p = []
    calc = [[nmax for i in range(n + 1)] for i in range(n + 1)]

    for i in range(n):
        (a,b) = map(int,input().split())
        p.append(a)
    else:
        p.append(b)

    for i in range(n+1):
        calc[i][i] = 0

    for i in range(1,n):
        calc[i][i+1] = p[i-1] * p[i] * p[i +1] 
    
    for s in range(2,n):
        for i in range(1,n + 1 - s ):
#            print (i,i+s)
            for j in range(s):
                m = calc[i][i+j] + calc[i+j+1][i+s] + p[i-1]*p[i+j]* p[i+s]
#                print ("m=",m,"calc:",i,i+j,"+calc",i+j+1,i+s,"p:",i-1,i+j,i+s)
                if calc[i][i+s] > m:
                    calc[i][i+s] = m
    print (calc[1][n])
if __name__ == '__main__':
    main()