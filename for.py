for i in [0, 1, 2, 3, 4]:
    print(i)

my_list = [0, 1, 2, 4]
for i in my_list:
    print(i)

my_list = [0, 1, 4, 9, 16, 25, 36]
for i in my_list:
    if i % 2 == 0:
        print(i)

my_list = ['tokyo', 'osaka', 'fukuoka', 'aichi', 'kyoto', 'chiba', 'saitama', 'gunma']
my_list_6 = []
for s in my_list:
    if len(s) >= 6:
        my_list_6.append(s)
print(my_list_6)

my_list = [1, 1, 2, 3, 5, 8, 13]
x = 0
for n in my_list:
    if n % 2 != 0:
        x += n
print(x)

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(10, 20, 3):
    print(i)

print(range(5))
print(list(range(5)))

for s in 'hoge':
    print(s)

for x in range(5):
    if x == 2:
        break
    print(x)

for x in range(5):
    if x == 2:
        continue
    print(x)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(10):
    if i % 2 == 0:
        break
    print(i)

numbers = [1, 1, 2, 3, 5, 8, 13, 21]
x = 0
for n in numbers:
    if n > 10:
        break
    x += n


