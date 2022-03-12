num_people = int(input(">>"))
#공포도는 영어로 fear
data = list(map(int, input(">>").split()))

result = 0
count = 0

for i in data:
    count += 1
    if count >=i:
        result +=1
        count = 0

print(result)