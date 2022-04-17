xlist = list(range(-100, 101, 20)) #-100부터 100까지 20씩 더해가며 리스트 생성

for num in xlist:
    print(num, end = ' ')

print(xlist[1] + xlist[-2])