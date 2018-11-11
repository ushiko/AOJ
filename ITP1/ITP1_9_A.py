word =str(input()).lower()
cnt = 0
while True:
    try:
        m = str(input())
    except EOFError:
        break
    if ( m == "END_OF_TEXT"):
        break
    for i in  m.lower().split():
        if ( i == word):
            cnt += 1
print (cnt)
