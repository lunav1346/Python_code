class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self): # 덧셈
        result = self.first + self.second
        return result

    def sub(self): # 뺄셈
        result = self.first - self.second
        return result

    def mul(self): # 곱셈
        result = self.first * self.second
        return result

    def div(self): # 나눗셈
        result = self.first / self.second
        return result
        

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(100, 4)

print(a.add())
print(b.div())