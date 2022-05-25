# 1월 1일 요일숫자
def weekday_to_digit(day1) -> any:
    return weekdays.index(day1)


# 1/1 ~ month/day 까지 며칠?
def date_to_day_difference(month, day) -> any:
    d = -1 # 1월 1일이라 하루를 빼고 시작.
    for i in range(0, month-1):
        d += days_month[i]
    d += (days_month[month] - day)
    return d


# num에 해당하는 요일값을 return
def digit_to_weekday(num) -> any:
    return weekdays[((num + weekday_to_digit(day1)) % 7)]

# main
weekdays = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day1 = input("올해 1월 1일의 요일: ")
month = int(input("생일의 월: "))
day = int(input("생일의 일: "))

print("내 생일의 요일: ", digit_to_weekday(date_to_day_difference(month, day)))