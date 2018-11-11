
(m,n)=  map(int,input().split())

l = []
for i in range(0,m):
    l.append(list(map(int,input().split())))

l2 = []
for i in range(0,n):
    l2.append(int(input()))


for i in range(0,m):
    sum = 0
    for j in range(0,n):
        sum += l[i][j] * l2[j]
    print (sum)