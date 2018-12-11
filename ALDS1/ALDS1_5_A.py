#  http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=jp
#  Exhaustive Search : python3
#  2018.12.08 yonezawa


#from collections import deque
import sys
input = sys.stdin.readline
import cProfile

p = [pow(2,i) for i in range(30)]

def checkSum(l,d,ck=0):
    td = 0
    for i in range(len(l)):
        if  p[i] & ck == p[i]:
            continue
        td += l[i]
    if (td < d):
        return False
    elif ( td == d ):
        return True

    for i in range (len(l)):
        if  p[i] & ck == p[i]:
            continue
        ck += p[i]
        if  checkSum(l,d,ck):
            return True
        d -= l[i]
        #print ("debug:",i,d,ck)
        if d == 0:
            return True
        elif d < 0:
            return False
        if  checkSum(l,d,ck):
            return True
    return False

def main():
    n1 = int(input())
    l1 = list(map(int,input().split()))
    l1.sort()
    l1.reverse()
    n2 = int(input())
    l2 = list(map(int,input().split()))
    for i in range(n2):
        if checkSum(l1,l2[i]):
            print ("yes")
        else:
            print ("no")

if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()