class person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('안녕하세요, 저는 {0}입니다.\n나이는 {1}살이며, 사는 곳은 {2}입니다.'.format(self.name, self.age, self.address))
    
maria = person('마리아', 20, '인천광역시 계양구')
maria.greeting()

print("이름:", maria.name)
print("나이:", maria.age)
print("주소:", maria.address)