# 특정 요일(string 타입)인 day1에 해당하는 요일에 대응하는 숫자를 돌려준다.
def weekday_to_digit(day1):
    return weekdays.index(day1)

# 1/1 ~ month/day (integer 타입)까지의 일수차 값을 돌려준다.
def date_to_day_difference(month, day):
    d = -1
    for i in range(0, month-1):
        d += daysinmonth[i]
    d += day
    return d

def birth_date_to_day_difference(birth_month, birth_day):
    d = -1
    for i in range(0, birth_month-1):
        d += daysinmonth[i]
    d += birth_day
    return d

# num에 해당하는 요일값을 돌려준다.
def digit_to_weekday(num):
    return weekdays[((num + weekday_to_digit(day1)) % 7)]


# main 부분
weekdays=["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
daysinmonth=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day1 = input("오늘 요일: ")
month = int(input("오늘 월: "))
day = int(input("오늘 월: "))

birth_month = int(input("생일의 월: "))
birth_day = int(input("생일의 일: "))

print("오늘부터 생일까지의 일수 차:", birth_date_to_day_difference(birth_month, birth_day) - date_to_day_difference(month, day))
print(digit_to_weekday(birth_date_to_day_difference(birth_month, birth_day) - date_to_day_difference(month, day)))