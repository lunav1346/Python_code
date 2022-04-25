name = input("이름: ")
number = input("학번: ")
major = input("전공: ")
birth = input("생일(년/월/일): ")

mydict = {'이름':name, '학번':number, '전공':major, '생일':birth}


print('저는', mydict['전공'], mydict['학번'], mydict['이름']+'이고,', '제 생일은', mydict['생일']+'입니다.')