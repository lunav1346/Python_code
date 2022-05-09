a, b, c = map(int, input("a, b, c를 입력하세요: ").split())
# a가 범위
# b의 배수 출력
# c의 배수 출력
for i in range(b, a+1, b):
    print(i, end = " ")

print()

for i in range(c, a+1, c):
    print(i, end = " ")