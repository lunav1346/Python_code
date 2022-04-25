#5페이지
i = 0
while i < 100:
    print("Hello, World!")
    i+=1

#6페이지
i = 1
while i < 101:
    print("Hello, World!")
    i+=1

#7페이지
i = 100
while i > 0:
    print("Hello, World", i)
    i-=1

#8페이지
count = int(input('반복할 횟수'))
i = 0
while i < count:
    print("Hello, World!", i)
    i+=1

count = int(input('반복할 횟수를 입력하세요: '))
while count > 0:
    print("Hello, world!", count)
    count -= 1

#9페이지
while True:
    print("Hello, World!")

#10페이지
while 1:
    print('Hello, World!')

while 'Hello':
    print("Hello, World!")

#13페이지
for i in range(100):
    print("Hello", i)

#14페이지
for i in range(5, 12):
    print("Hello, World!",i)

for i in range(0, 10, 2):
    print("Hello, World!", i)

#16페이지
for i in range(10, 0, -1):
    print("Hello, World!", i)

#18페이지
count = int(input("반복할 횟수를 입력해주세요: "))
for i in range(count):
    print("Hello, World!", i)

#19페이지
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

#20페이지
for letter in 'python':
    print(letter, end = ' ')


#21페이지
i = 0
while True:
    print(i)
    i += 1
    if i == 100:
        break

#23페이지
while True:
    line = input(">")
    if line == 'done':
        break
    print(line)
print('Done!')

#24페이지
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)

#25페이지
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)