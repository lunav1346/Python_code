
name = input("이름: ")
number = input("학번: ")
major = input("전공: ")
birth = input("생일(년/월/일): ")

mydict = {'이름':name, '학번':number, '전공':major, '생일':birth}
# 위에서 입력받은 값을 mydict 딕셔너리로 만들기


# print('저는', mydict['전공'], mydict['학번'], mydict['이름']+'이고,', '제 생일은', mydict['생일']+'입니다.')
print(f'저는 {mydict["전공"]} {mydict["학번"]} {mydict["이름"]}이고, 제 생일은 {mydict["생일"]}입니다.')


#또는

dic = {}
dic["name"] = input("이름: ")
dic["number"] = input("학번: ")
dic["major"] = input("전공: ")
dic["birth"] = input("생일(연/월/일): ")
# 입력받는 변수를 바로 dic 딕셔너리에 대입

print(f'저는 {dic["major"]} {dic["number"]} {dic["name"]}이고, 제 생일은 {dic["birth"]}입니다.')