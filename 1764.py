N, M = map(int, input().split())

a = set()
for i in range(N):
    a.add(input())

b = set()
for j in range(M):
    b.add(input())

result = sorted(list(a & b))
print(len(result))

for i in result:
    print(i)