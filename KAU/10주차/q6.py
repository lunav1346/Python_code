the1_time = ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
the1_chk = [False, False, False, False, False, False]

the2_time = ["13:05", "14:05", "15:05", "16:05", "17:05", "18:05"]
the2_chk = [False, False, False, False, False, False]

the3_time = ["13:10", "14:20", "15:30", "16:40", "17:50"]
the3_chk = [False, False, False, False, False]

<<<<<<< HEAD
'''
=======

>>>>>>> 5d8f17be2046b57a1a2e82c673f3f2511a8ff54b
while True:
    user_input = int(input("1, 2, 3 중 테마방 번호를 선택하세요. 0을 입력하면 이 프로그램은 끝납니다: "))
    if user_input == 0:
        print("감사합니다.")
        break

    elif user_input == 1:
        for i in the1_time:
            print(i, end = " ")
            
    elif user_input == 2:
        for i in the2_time:
            print(i, end = " ")

    elif user_input == 3:
        for i in the3_time:
            print(i, end = " ")

    else:
        print("해당 테마방은 없습니다.", end = "")
    
    print()
<<<<<<< HEAD
'''

while True:
    a = int(input("1, 2, 3 중 테마방 번호를 선택하세요. 0을 입력하면 이 프로그램은 끝납니다: "))
    if a == 1:
        for i in range(len(the1_time)):
            if the1_chk[i] == False:
                print(the1_time[i], end = " ")
        print()

    elif a == 2:
        for i in range(len(the2_time)):
            if the2_chk[i] == False:
                print(the2_time[i], end = " ")
        print()

    elif a == 3:
        for i in range(len(the3_time)):
            if the3_chk[i] == False:
                print(the3_time[i], end = " ")
        print()

    elif a == 0:
        print("감사합니다.")
        break

    else:
        print("해당 테마방은 없습니다.", end = " ")
=======

>>>>>>> 5d8f17be2046b57a1a2e82c673f3f2511a8ff54b

