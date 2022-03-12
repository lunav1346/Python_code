class person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount
        # == self.__wallet = self.__wallet - amount
        print('이제 {0}원 남았네요'.format(self.__wallet))

maria = person('maria', 20, '인천시', 100000)
maria.pay(2000)