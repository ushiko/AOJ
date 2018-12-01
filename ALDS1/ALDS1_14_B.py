# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_A&lang=jp
#  Naive String Search : python3
#  2018.11.26 yonezawa

import sys
input = sys.stdin.readline
#import cProfile

def main():
    s1  = str(input()).rstrip('\n')
    s2  = str(input()).rstrip('\n')
    
    s1_len = len(s1)
    s2_len = len(s2)
    sc = 1
    for k in range(1,len(s2)):
        if s2[0] != s2[k]:
            break
        sc += 1
    tc = len(set(s2))

    if (tc == 1 and s2_len > 1):
        cnt = 0
        for k in range(s1_len ):
            if (s1[k] == s2[0]):
                cnt += 1
            else:
                cnt = 0
            if (cnt >= s2_len ):
                print (cnt - s2_len)
    else:
        i = s1.find(s2)
        while i != -1 :
            print (i)
            i = s1.find(s2,i+1)


if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()
