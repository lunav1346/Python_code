data = input(">>")

#입력받았던 첫 번째 문자를 정수로 캐스팅한 후 대입
result = int(data[0])

#i가 1부터 data str의 길이만큼.
for i in range(1, len(data)):
    #하나라도 0 또는 1인 경우 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num

print(result)