# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C&lang=jp
#   Doubly Linked List : python3
#  2018.11.27 yonezawa


from collections import deque

import sys
input = sys.stdin.readline
import cProfile

class LinkedList:
    def __init__(self):
        self.data = None
        self.back = None
        self.front = None
        self.cnt = 0
    def push_front(self,d):
        self.cnt += 1
        i = self
        if i.front == None or i.back == None:
            i.front = LinkedList()
            i.front.data = d
            i.front.back = i
            i.front.front = i
            self.back = i.front
            return
        i = self.back
        i.front = LinkedList()
        i.front.data = d
        i.front.back = i
        i.front.front = self
        self.back = i.front
    def push_back(self,d):
        i = self
        self.cnt += 1
        if i.back == None or i.front == None:
            i.back = LinkedList()
            i.back.data = d
            i.back.front = i
            i.back.back = i
            self.front = i.back
            return
        i = self.front
        i.back = LinkedList()
        i.back.data = d
        i.back.front = i
        i.back.back = self
        self.front = i.back
    def front_list(self):
        i = self.front
        l = []
        while i != None and i.data != None:
            l.append(i.data)
            i = i.front
        return l
    def back_list(self):
        i = self.back
        l = []
        while i != None and i.data != None:
            l.append(i.data)
            i = i.back
        return l

    def del_num(self,n):
        i = self.front
        while i.data != None:
            if (i.data == n):
                if i.front.data == None:
                    t = i.back
                    t.front = self
                    self.back = t
                else:
                    t = i.back
                    t.front = i.front
                    i.front.back = t
                self.cnt -= 1
                return True
            i = i.front
            
        return False

    def pop_front(self):
        if ( self.front == None ):
            return None
        self.cnt -= 1
        t = self.front.data
        i = self.front.front
        if ( i.data == None ):
            self.front = None
        else:
            self.front = i
            i.back = self
        return t
    def pop_back(self):
        if ( self.back == None ):
            return None
        self.cnt -= 1
        t = self.back.data
        i = self.back.back
        if ( i.data == None ):
            self.back = None
        else:
            self.back = i
            i.front = self
        return t

def main():
    node = LinkedList()
    n =  int(input())
    skipFlag = False
    while n > 0:
        if skipFlag == False:
            l = list(map(str,input().split()))
        skipFlag = False
        cmd = l[0]
        if ( cmd == 'insert'):
            d = int(l[1])
            if n <= 1:
                node.push_back(d)
                n -= 1
                continue
            l = list(map(str,input().split()))
            if len(l) == 0:
                node.push_back(d)
                break
            if (l[0] == 'deleteFirst' ):
                n -= 1
                continue
            if (node.cnt == 0 and l[0] == 'deleteLast'):
                n -= 1
                continue
            skipFlag = True
            node.push_back(d)
        elif ( cmd == 'delete'):
            node.del_num(int(l[1]))
        elif ( cmd == 'deleteFirst'):
            node.pop_front()
        else:
            node.pop_back()
        n -= 1
#        print (node.cnt,n)
#        print (*l)
#        print (*node.front_list())
#        print (*node.back_list())
#    print (*node.front_list())
    print (node.cnt)

if __name__ == '__main__':
#   main()
    pr = cProfile.Profile()
    pr.runcall(main)
    pr.print_stats()