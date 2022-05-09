import time

input("엔터를 누르고 속으로 10초를 셉니다.")
start = time.time()

input("10초라고 생각들면 엔터를 칩니다.")
end = time.time()

record = end - start
print(f"내가 센 시간과 실제 시간의 차이: {abs(10-record)}")