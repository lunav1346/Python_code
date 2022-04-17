a: str = list(input() for i in range(4))

for i in a: print(i)

b : str = len(a[0])+len(a[1])+len(a[2])+len(a[3]) + 3
#개행문자의 수 = (줄수 - 1)
#개행문자는 input으로 받아지지 않으므로 줄수-1만큼 더하기.


print(f'{b}자')
