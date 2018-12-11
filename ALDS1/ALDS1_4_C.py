# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=jp
#  Binary Search : python3
#  2018.12.08 yonezawa


#from collections import deque
#import sys
#input = sys.stdin.readline
#import cProfile

def main():
    dic = {}
    for i in range(int(input())):
        l = list(map(str,input().split()))
        if l[0] == 'insert':
            dic[l[1]] = 'yes'
        else:
            try:
                print (dic[l[1]] )
            except:
                print ('no')
if __name__ == '__main__':
   main()
#    pr = cProfile.Profile()
#    pr.runcall(main)
#    pr.print_stats()