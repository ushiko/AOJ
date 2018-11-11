alpha = "abcdefghijklmnopqrstuvwxyz"
t = ""
while True:
    try:
        n  =  str(input()).lower()
    except EOFError:
        break
    t = t + n

for i in alpha:
    print (i,":",t.count(i))
