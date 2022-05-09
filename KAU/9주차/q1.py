i = 1

while i < 6:
    j = 0
    while j < 6-i:
        print(" ", end = "")
        j += 1
    
    k = 0
    while k < 2*i -1:
        print("*", end = "")
        k +=1
    print()

    i +=1