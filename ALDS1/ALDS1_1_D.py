#Maximum Profit
#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D&lang=jp

n = int(input())
min = int(input())
profit = -999999999

for i in range(0,n-1):
    s = int(input())
    if (s - min > profit):
        profit = s - min
    if (min > s):
        min = s
print (profit)
