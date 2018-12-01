

max = 10000
j = 3
l = [1] * (max + 1)
l[1] = 0
for i in range(4,max + 1, 2):
    l[i] = 0

for i in range(3,max + 1, 2):
    if ( l[i] == 0 ):
        continue
    j = i + i 
    while ( j <= max ):
        l[j] = 0
        j = j + i 


while True:
    try:
        k = int(input())
    except EOFError:
        break
    cnt = 0
    for i in range(1,k+1):
        if (l[i] + l[k+1-i] == 2 ):
            cnt += 1
    print(cnt)