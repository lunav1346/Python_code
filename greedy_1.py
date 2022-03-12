count = 0
N, K = map(int, input("숫자를 입력하세요\n>>").split())
#띄어쓰기로 나눈다, int로 변환

while N != 1:
    if N % K == 0:
        N /= K
        count +=1
        if N == 1:
            break
    else:
        N -= 1
        count +=1
        if N == 1:
            break

print(count)