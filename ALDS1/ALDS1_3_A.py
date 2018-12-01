# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A&lang=jp
#  Stack : python3
#  2018.11.26 yonezawa

from collections import deque
import sys
input = sys.stdin.readline

def calc(q):
    tq = deque()
    for i in range(len(q)):
        op = q.popleft()
#        print ("debug:",op)
        if ( op == '+' ):
            a = tq.pop()
            b = tq.pop()
            tq.append(b+a)
        elif (op == '-' ):
            a = tq.pop()
            b = tq.pop()
            tq.append(b-a)

        elif (op == '*' ):
            a = tq.pop()
            b = tq.pop()
            tq.append(b*a)
        elif (op == '/' ):
            a = tq.pop()
            b = tq.pop()
            tq.append(b//a)
        else:
            tq.append(int(op))
    return tq.pop()

def main():
    q = deque(map(str,input().split()))
    print (calc(q))

if __name__ == '__main__':
    main()