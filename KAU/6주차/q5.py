a = input("문자열 입력: ")
b = a[2] + a[-2]

print(b)

if b in a:
    print("True")
else:
    print("False")