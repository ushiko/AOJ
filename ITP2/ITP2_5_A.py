# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_5_A&lang=jp
# Sorting Pairs

import sys
input = sys.stdin.readline

def main():
    l = []
    for i in range(int(input())):
        (a,b) = map(int,input().split())
        l.append((a,b))
    for a,b in sorted(l):
        print (a,b)
if __name__ == '__main__':
    main()