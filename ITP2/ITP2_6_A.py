# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_6_A&lang=jp
#  Binary Search : python3
#  2018.11.26 yonezawa

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    l = list(map(int,input().split()))

    for i in range(int(input())):
        max = n -1
        min = 0
        mid = max // 2
        d = int(input())
        while True:
            if (l[mid] > d ):
                max = mid
            elif (l[mid] == d ):
                print ("1")
                break
            else:
                min = mid
            mid =  (max + min ) // 2 
            if ( mid == max or mid == min ):
                if ( l[mid] == d or l[max] == d):
                    print ("1")
                    break
                #print ("debug:",min,mid,max,l[mid])
                print ("0")
                break

if __name__ == '__main__':
    main()