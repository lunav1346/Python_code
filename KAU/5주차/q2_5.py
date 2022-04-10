a = int(input("중간고사 점수를 입력하세요: "))
b = int(input("기말고사 점수를 입력하세요: "))
avg = (a+b)/2 #a, b의 평균
if avg >= 90:
    print("훌륭하네요")
elif avg >= 80:
    print("잘했어요")
elif avg >= 70:
    print("조금 더 공부하세요")
else:
    print("내년에 다시 봐요")