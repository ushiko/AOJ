# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_2_D&lang=jp
# Splice


import sys
input = sys.stdin.readline
import cProfile
import time

def loop_proc():
    wl = []
    (n1,n2) = map(int,input().split())
    wl = ['' for i in range(n2)]
    for i in range(n2):
        l = list(map(str,input().split()))  
        if (l[0] == "0" ):
            wl[int(l[1])] += " " + l[2]
        elif (l[0] == "1" ):
            #print (wl[int(l[1])].strip())
            sys.stdout.writelines(wl[int(l[1])].strip())
        else:
            wl[int(l[2])]+=  wl[int(l[1])]
            wl[int(l[1])] = ""

#loop_proc()
pr = cProfile.Profile()
pr.runcall(loop_proc)
pr.print_stats()