
(n,m,l)=  map(int,input().split())

g1 = []
for i in range(0,n):
    g1.append(list(map(int,input().split())))

g2 = []
for i in range(0,m):
    g2.append(list(map(int,input().split())))

for i in range(0,n):
    t = []
    for j in range(0,l):
        sum = 0
        for k in range(0,m):
            sum += g1[i][k]*g2[k][j]
        t.append(sum)
    print (' '.join(map(str,t))) 