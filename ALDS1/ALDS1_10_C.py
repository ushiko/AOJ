# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=jp
# Longest Common Subsequence: python3
#  2018.12.04 yonezawa

import sys
input = sys.stdin.readline
import cProfile
def main():
    n = int(input())

    for i in range(n):
        s1 = str(input()).strip()
        s2 = str(input()).strip()
        calc = [[0 for i in range(len(s2)+1)] for i in range(len(s1)+1)]        
        for j in range(1,len(s1)+1):
            for k in range(1,len(s2)+1):
                #print (j,k)
                if s1[j-1] == s2[k-1] :
                    calc[j][k] = 1 + calc[j-1][k-1]
                elif calc[j-1][k] > calc[j][k-1]:
                    calc[j][k] = calc[j-1][k]
                else:
                    calc[j][k] = calc[j][k-1]
        print (calc[j][k])

if __name__ == '__main__':
    #main()
    pr = cProfile.Profile()
    pr.runcall(main)
    pr.print_stats()