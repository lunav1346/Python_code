a = int(input('입력: '))
for i in range(1, a+1):
    if i % 2 == 1:
        print(i, end=' ')

print()

for i in range(1, a+1):
    if i % 2 == 0:
        print(i, end = ' ')