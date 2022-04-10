a = int(input())
count = 0
if a >= 100 or a < 1: #100 이상이거나, 양수가 아니면 출력
    print("범위에 맞는 수를 입력하세요!")

else:
    a = str(a)
    count = count + a.count('3')
    count = count + a.count('6')
    count = count + a.count('9')
    for i in range(count):
        print("짝")
    #3, 6, 9의 개수를 센 다음 개수만큼 짝을 하나씩 출력.
