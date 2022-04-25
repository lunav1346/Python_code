depth = 300
day = 0

while (depth > 0):
    day += 1
    depth -=55
    if depth < 0:
        break
    depth +=13
print(day, "일")