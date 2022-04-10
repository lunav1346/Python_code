# import winsound
import time
bot_prmpt = "Bot >" #Bot > 을 채팅로봇이 말할때마다 띄운다.
user_prmpt = "User > " #User > 을 사람이 입력할때마다 띄운다.

print("%s 안녕하세요." %bot_prmpt)
# winsound.Beep(700, 500)
time.sleep(0.5) #0.5초 쉰다?

print("%s 나는 인공지능 채팅 로봇입니다." %bot_prmpt)
# winsound.Beep(700, 500)
time.sleep(0.5)

print("%s 당신의 이름은 무엇인가요?." %bot_prmpt)
name = input(user_prmpt)
# winsound.Beep(700, 500)
time.sleep(0.5)

print("%s %s 님, 만나서 반가워요" %(bot_prmpt, name))
# winsound.Beep(700, 500)
time.sleep(0.5)

print("%s 당신의 고향은 어디인가요?" %bot_prmpt)
gohyang = input(user_prmpt)
print("%s %s 님은 %s 에서 왔군요." %(bot_prmpt, name, gohyang))
time.sleep(0.5)

print("%s %s 님은 어느 학교를 다니나요?" %(bot_prmpt, name))
school = input(user_prmpt)
time.sleep(0.5)

print("%s %s 님의 전공은 무엇인가요?" %(bot_prmpt, name))
major = input(user_prmpt)
print("%s %s 님은 %s 에서 %s 를 공부하고 있군요." %(bot_prmpt, name, school, major))
time.sleep(0.5)

print("%s %s 님, 다음에 봐요" %(bot_prmpt, name))