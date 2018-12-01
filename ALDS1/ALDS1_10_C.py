# Longest Common Subsequence
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=jp

n = int(input())

while True:
    if ( n == 0):
        break
    n = n -1
    wl = {}
    wl2 = {}

    str2 = str(input())
    str1 = str(input())

    for i in set(str1):
        cl = []
        for j in range(0,len(str2)):
            if (i == str2[j]):
                cl.append(j)
        wl[i] = cl

    for i in set(str2):
        cl = []
        for j in range(0,len(str1)):
            if (i == str1[j]):
                cl.append(j)
        wl2[i] = cl

    print (str1,str2,wl,wl2)
    max_cnt = 0
    for i in range(0,len(str1)):
        pos = cnt = 0
        for j in str1[i:]:
            tl = []
            tl = list(filter(lambda a: a >= pos , wl[j]))
            print ("cnt=",cnt," pos=",pos," len=",len(str2)," j=",j,sep="")
            print ("targetlist:",tl)
            print (str1[i:],str2[:pos],str2[pos:])
            if (len(tl) < 1):
                break
            cnt += 1
            print ("pos:",pos,"->",tl[0]+1)
            pos = tl[0] + 1
        if (cnt > max_cnt):
            max_cnt = cnt
        print("###############################")
    print (max_cnt)

