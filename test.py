from itertools import combinations

a = input()
b = []

list_a = list(str(a))

for i in combinations(list_a, int(a)):

    b.append("".join(i))

print(b)