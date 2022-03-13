import sys

while True:
    a = input()
    panjeong = 'Y'

    if a == "*":
        break
    else:
        for i in range(97, 123):
            if a.find(chr(i)) == -1:
                panjeong = 'N'
                break
    
    print(panjeong)