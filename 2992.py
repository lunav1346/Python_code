a = int(input())
sor_a = list(str(a))
sor_a.sort()
#작은거에서 큰 순서대로 나열

sor_a.insert(0, sor_a[-1])
#0번자리에 -1번(맨 마지막꺼를 정렬)

del sor_a[-1]
#-1번(맨 마지막꺼)를 없앰

b = "".join(sor_a)
b = int(b)
#97251이였다면 91257을 출력

if a >= b:
    print(0)
else:
    print(b)