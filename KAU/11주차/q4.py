import math
def get_areaTrapezoid():
    a = int(input("윗변의 길이: "))
    b = int(input("아랫변의 길이: "))
    h = int(input("높이의 길이: "))
    return (a + b) * h * 0.5
def get_areaParallelogram():
    a = int(input("윗변의 길이: "))
    h = int(input("높이의 길이: "))
    return a * h
def get_areaRectangle():
    a = int(input("윗변의 길이: "))
    h = int(input("높이의 길이: "))
    return a * h
def get_areaRhombus():
    a = int(input("너비의 길이: "))
    b = int(input("높이의 길이: "))
    return a * b * 0.5
def get_areaSquare():
    a = int(input("한 변의 길이: "))
    return a ** 2
def get_areaCircle():
    r = int(input("반지름의 길이: "))
    return r ** 2 * math.pi
print("넓이를 구하고 싶은 도형의 번호를 넣으세요")
shape = int(input("1: 사다리꼴, 2: 평행사변형, 3: 직사각형, 4: 마름모, 5: 정사각형, 6: 원"))
if shape == 1:
    print(f"사다리꼴의 넓이: {get_areaTrapezoid()}")
elif shape == 2:
    print(f"평행사변형의 넓이: {get_areaParallelogram()}")
elif shape == 3:
    print(f"직사각형의 넓이: {get_areaRectangle()}")
elif shape == 4:
    print(f"마름모의 넓이: {get_areaRhombus()}")
elif shape == 5:
    print(f"정사각형의 넓이: {get_areaSquare()}")
elif shape == 6:
    print(f"원의 넓이: {get_areaCircle()}")