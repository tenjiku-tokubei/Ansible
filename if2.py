a = 20
if a >= 10:
    print(a)

if 'a' in ['a', 'b', 'c']:
    print('OK')

a = 20
b = 10
if a > 10 and b < 15:
    print('OK')

print(bool(1))
print(bool(0))

a = 0
if a == 0:
    a += 1
    a *= 2
    a -= 1
    print(a)

if a >= 10:
    print('OK')
else:
    print('NG')

a = 30
if a % 15 == 0:
    print('fifteen')
elif a % 3 == 0:
    print('three')
elif a % 5 == 0:
    print('five')
else:
    pass

a, b = 10, 20
if a > 10 and b > 10:
    print('OK')
else:
    print('NG')

a = 10
if a > 10:
    a /= 2
else:
    a += 1
print(a)

a = 10
if a >= 100:
    a *= 2
elif a >= 50:
    a /= 2
else:
    a +=2
print(a)
