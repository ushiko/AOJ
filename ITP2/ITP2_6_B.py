# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_6_B&lang=jp
#  Includes : python3
#  2018.11.26 yonezawa

import sys
input = sys.stdin.readline

def binsearch(d,l):
    max = len(l) -1
    min = 0
    mid = max // 2
    while True:
        if (l[mid] > d ):
            max = mid
        elif (l[mid] == d ):
            return True
        else:
            min = mid
        mid =  (max + min ) // 2 
        if ( mid == max or mid == min ):
            if ( l[mid] == d or l[max] == d):
                return True
            return False

def main():
    n1 = int(input())
    l1 = list(map(int,input().split()))
    n2 = int(input())
    l2 = list(map(int,input().split()))
    for i in l2:
        result = binsearch(i,l1)
#        print ("test:",result,i,l1)
        if ( result == False ):
            print (0)
            return
    else:
        print (1)

if __name__ == '__main__':
    main()