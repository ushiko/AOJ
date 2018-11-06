
i = 1
while True:
    try:
      (n)  =  int(input())
    except:
     exit
    if ( n == 0):
        break
    print ('Case {}: {}'.format(i,n))
    i += 1

