def multiple(a, b):
    for i in range(1, a+1):
        for j in range(1, b + 1):
            if (i + j) % 3 == 0:
                print(f'({i}, {j})')

multiple(6, 6)