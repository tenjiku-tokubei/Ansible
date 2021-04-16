a = 1
while a <= 10:
    print(a)
    a += 1

a, b = 0, 1
while b < 20:
    print(b)
    a, b = b, a + b

a = 1
while True:
    if a % 2 == 0:
        print(a)
    a += 1
    if a > 100:
        break

a = 0
while a < 100:
    if a > 10:
        break
    a += 2

