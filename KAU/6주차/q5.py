a = input("문자열 입력: ")
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