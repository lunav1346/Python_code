'''for i in range(5):
    for j in range(5):
        if i >= j:
            print("*", end = "")
    print()

print()

a = int(input())
for i in range(a):
  for j in range(a-i-1):
    print(' ',end='')
  for j in range(2*i+1):
    print('*',end='')

  print()

print()

for i in range(5):
    for j in range(5):
        if i <= j:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

x = 10
y = 3
def get_quotient_remainder(a, b):
    return 10//3, 10 %3

quotient, remainder = get_quotient_remainder(x, y)
print(f'몫: {quotient}, 나머지: {remainder}')