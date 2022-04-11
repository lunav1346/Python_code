import sys

divide = 0 #몫
nam = 0 #나머지

a = int(sys.stdin.readline())
fivemin = onemin = tensec = 0


while a != 0:
    if a % 10 > 1:
        print(-1)
        break

    elif a // 300 >= 1:
        a -= 300
        fivemin += 1

    elif a // 60 >= 1:
        a -= 60
        onemin += 1

    elif a // 10 >= 1:
        a -= 10
        tensec += 1

print(fivemin, onemin, tensec)