num_list = [3, 6, 9]
a = int(input("1부터 10 미만의 수를 입력하세요: "))

<<<<<<< HEAD
if a >= 10 or a < 0:
    print('범위에 맞는 수를 입력하세요.')
elif a in num_list:
    print("짝" * a )
else:
=======
if a >= 10 or a < 0: #범위 밖의 수 입력시 출력
    print('범위에 맞는 수를 입력하세요.')

elif a in num_list: #입력한 a가 num_list 안에 있다면 짝을 a번 출력
    print("짝" * a )

else: #입력한 a가 num_list 안에 없다면 출력
>>>>>>> a1f3d0c60fe7893129e933295cc08adc0c43dba5
    print("3 또는 6 또는 9가 아닌 숫자네요.")