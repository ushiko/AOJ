
try:
     (n)  =  int(input())
except:
    exit

hh = n // 3600
mm = (n % 3600 ) // 60
ss = n % 60

#print ('{:0=2}:{:0=2}:{:0=2}'.format(hh,mm,ss))
print ('{}:{}:{}'.format(hh,mm,ss))