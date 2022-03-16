numlist = list(map(int, input().split()))

sorted_Numlist = numlist.sort()

while sorted_Numlist != numlist:
    if numlist[0] > numlist[1]:
        numlist[0], numlist[1] = numlist[1], numlist[0]
        print("".join(numlist))
    else:
        continue

    if numlist[1] > numlist[2]:
        numlist[1], numlist[2] = numlist[2], numlist[1]
        print("".join(numlist))
    else:
        continue

    if numlist[2] > numlist[3]:
        numlist[2], numlist[3] = numlist[3], numlist[2]
        print("".join(numlist))
    else:
        continue

    if numlist[3] > numlist[4]:
        numlist[3], numlist[4] = numlist[4], numlist[3]
        print("".join(numlist))
    else:
        continue

    if numlist[4] > numlist[5]:
        numlist[4], numlist[5] = numlist[5], numlist[4]
        print("".join(numlist))
    else:
        continue

    if numlist == sorted_Numlist:
        print("".join(numlist))
        break

