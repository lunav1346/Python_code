a = list(input() for i in range(4))

for i in a:
    print(i)

b = len(a[0])+len(a[1])+len(a[2])+len(a[3]) + 3
'''마지막에 +3을 하는 이유는 '어린', '내', '수비' 다음 엔터를 쳐 공백을 만들기 때문인데, 
    a = list(input() for i in range(4))의 경우 끊는 단위가 엔터이기 때문에 엔터로 생기는 공백까지 포함하지 않는다.
    따라서 엔터를 쳤을 때 생기는 공백 3자를 포함해 +3을 해주어야 한다.
'''

print(str(b)+'자')
#풀어야함.