#6페이지
def Hello():
    print("Hello, World!")
Hello()

#7페이지
def hello():
    print("Hello, World!")
hello()

#13페이지
hello()
def hello():
    print("Hello, World!")

#18페이지
print(add(10, 20))
def add_sub(a, b):
    return a+b, a-b
x, y = add_sub(10, 20)
print(x)
print(y)

#21페이지
a = [10, 10, 10, 10, 10]
x = 0
for i in a:
    x += i
print(x)

def sum(num_list):
    sum_result = 0
    for num in num_list:
        sum_result += num
    
    return sum_result

a = [10, 10, 10, 10, 10]
sum(a)


#24페이지
print(10, 20, 30)
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

print_numbers(10, 20, 30)