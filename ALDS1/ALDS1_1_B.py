#Greatest Common Divisor
#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B&lang=jp

def gcd(a,b): 
    if ((a%b) == 0 ):
        return b
    else:    
        return (gcd(b,a%b))

(a,b) = map(int,input().split())
print (gcd(a,b))