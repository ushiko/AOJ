
n =  int(input())

mark = ["S","H","C","D"]

card = [1] * 52

while ( n > 0 ):
    (m,mn)  =  map(str,input().split())
    j = 0
    while (j < 4):
        if (m == mark[j]):
            break
        j = j +1
    card [(int(mn) -1 ) + j*13] = 0
    n = n -1

for i in range (0,52):
    if ( card[i] == 1 ):
        print (mark[i//13], (i % 13) +1)