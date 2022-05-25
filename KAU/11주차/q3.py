def compute_salary(x):
    print(x * 10000 if x <= 40 else (x-40)*15000 + 40*10000)

compute_salary(30)
compute_salary(45)