<<<<<<< HEAD
word = input("입력")
=======
<<<<<<< HEAD
a = input() # 숫자 입력받기.
b = None
alist = list()

for i in range(len(a)):
    alist.append(a[i])
    alist.sort()

print(b)
=======
<<<<<<< HEAD
#4
age = 12345
print(type(age))
print(id(age))
>>>>>>> b09ff948dbde8ab3a40029a9aec584fe59e5389d

def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

<<<<<<< HEAD
is_palindrome(word)
=======
x = int("2019")
y = int("2000")
print(x - y)
print(type(x))

year = input("몇 년도에 태어났나요? ")
age = 2019 - int(year) + 1
print("그럼 올해 %d 살이겠군요" %age)

year = int(input("몇 년도에 태어났나요? "))
age = 2018 - year + 1
print("그럼 올해 %d 살이겠군요" %age)

x = int("2002")
pi = float("3.14")
text = str(3.14)

#10
dict = {"강아지": "dog", "고양이" : "cat", "새": "bird"}
print(dict)
print(dict["강아지"])

#11
dict = {"강아지": "dog", "고양이" : "cat", "새": "bird"}
print(dict)
print(dict.keys())
print(dict.values())

for item in dict.items():
    print(item)

for item in dict.items():
    print(item)
    print(item[0])
    print(item[1])

#12
mydict = {}
mydict["홍길동"] = "010-1111-1111"
mydict["이순신"] = "010-2222-2222"
print(mydict)

mydict = {"홍길동":"010-1111-1111", "이순신": "010-2222-2222"}
print(mydict)
del mydict["이순신"]
print(mydict)

mydict.clear()
print(mydict)
del mydict
print(mydict)

#14
a = "ABC"
print(a[0])
print(a[1])
print(a[3])
print(len(a))

#15
a = "HELLO Python"
print(a[0])
print(a[0:5])
print(a[6:12])
print(a[-11:-8])
print(a[0:-7])

#16
a = "HELLO"
print(a[0])
print(a[-1])

print(a[0:4])
print(a[:3])
print(a[0:])

a = "save"
b = "earth"
print(a+b)

a = "panimalar"
print(a*3)

s = "good morning"
print("m" in s)
print("a" in s)

#17
x = 10
print("x is {}".format(x))
print("a = {}, b = {}".format(100, 200))
print("I am {} years old".format(20))
print("x is", x)
print("x = %d" %x)
print("x is {}".format(x))

#18
a = 'happy birthday'
a.capitalize()
a.upper()
a.lower()
a.title()
a.swapcase()
a.split()
a.center(19, "*")
a.count('happy')
a.replace('happy', 'wishyou happy')

b = "happy"
a = '-'
a.join(b)

a = 'happy birthday'
a.isupper()
a.islower()
a.isalpha()
a.isalnum()
a.isdigit()
a.isspace()
a.istitle()
a.startswith('h')
a.endswith('y')
a.find('happy')
len(a)
min(a)
max(a)

#21
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

a = [1, 2, 3]
a[0]
a[0] + a[2]
a = [1, 2, 3, ['a', 'b', 'c']]
a[0]
a[-1]
a[3]
a[-1][0]
a[-1][1]
a[-1][2]
a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]

#22
a[1, 2, 3, 4, 5]
a[0:2]

b = a[:2]
c = a[2:]
b
c

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]
a[3][:2]

a = [1, 2, 3]
b = [4, 5, 6]
a+b

a = [1, 2, 3]
a*3

a = [1, 2, 3]
len(a)

#23
a = [1, 2, 3]
a.append(4)
a

a = [1, 4, 3, 2]
a.sort()

a = ['a', 'c', 'b']
a.reverse()
a

a = [1, 2, 3]
a.index(3)
a.index(1)

a = [1, 2, 3]
a.insert(0, 4)
a
a.insert(3, 5)
a
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a = [1, 2, 3]
a.pop()
a

a = [1, 2, 3, 1]
a.count(1)

a = [1, 2, 3]
a.extend([4, 5])
a

b = [6, 7]
a.extend(b)
a
=======
while True:
    print('Hello')
>>>>>>> 697d05eb114b5e340e2d265869cd0d58c0baf66f
>>>>>>> 320eecc761e29050c169a010e338a1433dd34384
>>>>>>> b09ff948dbde8ab3a40029a9aec584fe59e5389d
