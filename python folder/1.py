a = input()
sl = {}
for i in a:
    if i in sl:
        sl[i] += 1
    else:
        sl[i] = 1
print(sl)