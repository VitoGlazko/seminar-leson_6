def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(2, 12):
    for j in range(1, i):
        if gcd(i, j) == 1:
            print(f"{j} / {i}")