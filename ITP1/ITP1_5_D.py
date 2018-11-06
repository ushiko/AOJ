
try:
     (n)  =  int(input())
except:
    exit

i = 1
end_check = False
while True:
    x = i
    if ( x % 3 == 0):
        print(' {}'.format(i),end="")
        end_check = True

    while end_check == False:
        if ( x % 10 == 3):
            print(' {}'.format(i),end="")
            end_check = True
        x = x // 10
        if (x == 0):
            end_check =True

    i += 1
    if (i > n ):
            break
    end_check = False
print ("")