a = input("문자열 입력: ")
b = a[2] + a[-2] #문자열의 3번째 글자와 마지막 2번째 글자를 이어 붙인 문자열을 출력

print(b)

if b in a: #문자열의 3번째 글자와 마지막 2번째 글자를 이어 붙인 문자열이 있다면 True, 없다면 False 출력
    print("True")
else:
    print("False")