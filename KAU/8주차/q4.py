while True:
    a = int(input("0이 아닌 숫자를 입력하시오. 끝내려면 0을 입력하세요: "))
    if a == 0:
        break
    else:
        for i in range(1, 10):
            print(f'{a} X {i} = {a*i}')