
i = 1
while True:
    try:
      (n)  =  int(input())
    except:
     exit
    if ( n == 0):
        break
    print ('case {}: {}'.format(i,n))
    i += 1

