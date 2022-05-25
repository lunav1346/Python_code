import random

def generate_randnum(start, end, num):
    a = list()
    for _ in range(num):
        a.append(random.randint(start, end))
    print(a); return a

def sum_randNum(m, n, o):
    sum = 0
    for i in generate_randnum(m, n, o):
        sum += i
    return sum

print(sum_randNum(1, 100, 5))
print(sum_randNum(1, 100, 5))