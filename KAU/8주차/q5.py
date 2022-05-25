depth = 300
day = 0

while (depth > 0):
    day += 1
    depth -=55
    if depth < 0:
        break
    depth +=13
print(f"{day}일")
# depth에서 직접 올라가고 내려가는 길이를 더하고 빼서 걸리는 날을 출력

# 또는

depth = 300
snail = 0
day = 0

while (depth >= snail):
    day += 1
    snail += 55
    if snail >= depth:
        break
    snail -= 13
print(f"{day}일")
#우물의 깊이 depth와 달팽이가 올라가는 거리 snail을 서로 비교해 걸리는 날을 출력