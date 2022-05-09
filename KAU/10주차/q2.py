# factorial() 정의
def factorial(n):
    j = 1
    for i in range(n, 0, -1):
        j*=i
    return j

n = int(input("입력값: "))
print(factorial(n))