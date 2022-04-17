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