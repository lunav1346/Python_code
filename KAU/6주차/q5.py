a = input("문자열 입력: ")
<<<<<<< HEAD
b : str = a[2] + a[-2] #문자열 2개를 붙여서 만듦.(String)
#var : type = value
#def fuction_name(parameter) -> type:
print(b)
'''
if b in a:
    print("True")
else:
    print('False')
    '''

print("True") if b in a else print("False")
=======
b = a[2] + a[-2] #문자열의 3번째 글자와 마지막 2번째 글자를 이어 붙인 문자열을 출력

print(b)

if b in a: #문자열의 3번째 글자와 마지막 2번째 글자를 이어 붙인 문자열이 있다면 True, 없다면 False 출력
    print("True")
else:
    print("False")
>>>>>>> a1f3d0c60fe7893129e933295cc08adc0c43dba5
