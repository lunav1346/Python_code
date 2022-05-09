#32페이지
largest_so_far = -1
loop_counter = 0
print("Before loop:", largest_so_far)

for num in [9, 41, 12, 3, 74, 15]:
    if num > largest_so_far:
        largest_so_far = num
    loop_counter +=1
    print(loop_counter, ":", largest_so_far, num)

print("After", largest_so_far)