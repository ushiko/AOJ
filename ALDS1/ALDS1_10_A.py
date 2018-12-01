#Fibonacci Number
#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=jp


class fibonacci:
    def __init__(self):
        self.result = [-1]*1000
        return 
    def calc(self,n):
        if (n == 0 or n == 1):
            self.result[n] = 1
            return 1
        if (self.result[n] != -1):
            return self.result[n]
        self.result[n-1] = self.calc(n-1) 
        self.result[n-2] = self.calc(n-2)
        return self.result[n-1] + self.result[n-2]
n = int(input())

print (fibonacci().calc(n))

