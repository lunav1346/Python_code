a = int(input("일한 시간: ")) #일한 시간 입력
if a <= 40: #일한 시간이 40시간 이하이면 시급 1만원으로 계산 후 출력
    wage = a * 10000 
    print("총 급료: %d" %wage)

else:
    wage = 40 * 10000 #기본 40시간은 시급 1만원으로 계산
    a -=40; wage = wage + (a * 15000) #40시간을 초과하는 금액은 15000원으로 계산 후 추가
    print("총 급료: %d" %wage)