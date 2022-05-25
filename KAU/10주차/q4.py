from pip import main


def even(a):
    if a % 2 == 0:
        return 1 
        # 짝수 = 1
    else:
        return 0
        # 홀수 = 0


def even_sum(a):
    j = 0
    for i in range(1, a+1):
        if even(i) == True:
            j += i
    return j
    
n = int(input("범위 시작의 양수 n: "))
m = int(input("범위 끝의 양수 m: "))

print(even_sum(m) - even_sum(n))
