i = 1
s = 0
count = 0

while count != 100:
    s = s + i
    if i > 0:
        i += 1
    else:
        i -= 1
    
    i *= -1

    count +=1
print(s)