while True:
    a = input()
    if a == '0':
        break
    else:
        if a == a[::-1]:
            print("yes")
        else:
            print("no")