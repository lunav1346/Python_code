# #4페이지
# for i in range(5):
#     for j in range(5):
#         print("*", end = "")
#     print()

# #8페이지
# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print("*", end = "")
#     print()
    
# for i in range(5):
#     for j in range(i):
#         # if j <= i:
#             print("*", end = "")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         # if j <= i:
#             print("*", end = "")
#     print()

# #10페이지
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("*", end = "")
#     print()

# #12페이지
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()

# #14페이지
# a = [38, 21, 53, 62, 19]
# i = 0
# while i < len(a):
#     print(a[i])
#     i+=1

# #15페이지
# a = [38, 21, 53, 62, 19]
# i = 0
# while i <= len(a): # 인덱스 에러 뜸
#     print(a[i])
#     i+=1

#22페이지
n = int(input())
s = 0
for i in range(1, n+1):
    s+=i

print(f"1 ~ {n}까지의 합: {s}")