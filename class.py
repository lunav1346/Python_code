class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    # 클래스의 함수는 메서드
    '''
    a.setdata(4, 2)가 있다고 해보자.
    메서드의 첫 번째 인자 self는 a.setdata의 a로 들어간다.
    두 번째 인자와 세 번째 인자인 first, second의 경우 각각 4, 2로 들어가게 된다.
    '''
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result


class MoreFourCal(FourCal):
    pass
