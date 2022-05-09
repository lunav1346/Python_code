command = input("뱀의 이동방향을 입력하십시오: ")

xylist = [0, 0] # [x, y]
lensnake = 1

for i in range(len(command)):

    if command[i] == "L":
        xylist[0] -= 1
    
    if command[i] == "R":
        xylist[0] += 1

    if command[i] == "U":
        xylist[1] += 1

    if command[i] == "D":
        xylist[1] -= 1

    if (xylist[0] == xylist[1]) and (xylist[0] != 0 and xylist[1] != 0):
        lensnake += 1
        
print("뱀의 길이는 %d 입니다" %lensnake)