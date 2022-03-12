'''class person:
    def greeting(self):
        print("Hello")
james = person()
james.greeting()

a = int(10)
b = list(range(10))
c = dict(x = 10, y = 20)
print(a)
print(b)
print(c)
'''

class person:
    def __init__(self):
        self.hello = '안녕하세요'
    
    def greeting(self):
        print(self.hello)
james = person()
james.greeting()