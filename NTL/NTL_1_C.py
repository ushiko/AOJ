from functools import reduce

def gcd(a,b): #最小公約数
    if ((a%b) == 0 ):
        return b
    else:    
        return (gcd(b,a%b))

def lcm(a,b):
    return a * b // gcd(a,b)

n = int(input())
l = list(map(int,input().split()))

print (reduce(lcm,l))