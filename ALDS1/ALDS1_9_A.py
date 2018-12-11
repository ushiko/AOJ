# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_8_C&lang=jp
# Binary Search Tree I
# 2018.12.01 yonezawa

import sys
input = sys.stdin.readline
import cProfile

def showHeap(li):
    #node 2: key = 8, parent key = 7, left key = 2, right key = 3,  
    for i in range(1,len(li)+1):
        n1=n2=n3=n4 =""
        p = i // 2
        r = i * 2 + 1
        l = i * 2
 
        n1 = "node {}: key = {}, ".format(str(i) , str(li[i-1]))
        if p > 0:
            n2 = "parent key = {}, ".format(li[p-1])
        if l -1 < len(li): 
            n3 = "left key = {}, ".format(li[l-1])
        if r -1 < len(li): 
            n4 = "right key = {}, ".format(li[r-1])
        
        print (n1+n2+n3+n4)
            
def main():
    n = int(input())
    l = list(map(int,input().split()))
    showHeap(l)

        
if __name__ == '__main__':
    main()
    #pr = cProfile.Profile()
    #pr.runcall(main)
    #pr.print_stats()