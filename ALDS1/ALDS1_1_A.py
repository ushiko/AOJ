#Insertion Sort
#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_A&lang=jp

n = int(input())
l = list(map(int,input().split()))
print (' '.join(map(str,l)))
for i in range(1,n):
    v = l[i]
    j = i -1
    while (j>=0 and l[j]>v ):
        l[j+1] = l[j]
        j -= 1
        l[j+1] = v
    print (' '.join(map(str,l)))
