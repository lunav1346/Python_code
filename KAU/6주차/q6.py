num_list = [3, 6, 9]
a = int(input("1부터 10 미만의 수를 입력하세요: "))

if a >= 10 or a < 0:
    print('범위에 맞는 수를 입력하세요.')
elif a in num_list:
    print("짝" * a )
else:
    print("3 또는 6 또는 9가 아닌 숫자네요.")