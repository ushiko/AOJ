# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_A&lang=jp
#  Vector
 
wl = []
for i in range(0,int(input())):
    l = list(map(str,input().split()))
    c = int(l[0])
 
    if ( c == 0 ):
        d = int(l[1])
        wl.append(d)
    elif(c == 1):
        d = int(l[1])
        print (wl[d])
    elif(c == 2):
        wl.pop()