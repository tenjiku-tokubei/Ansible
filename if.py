if True:
    print('True')
else:
    print('False')

x = 3
print(x > 1)

my_list = [0, 2, 4, 6, 8, 10]
print(2 in my_list)

my_str = 'This is a pen'
print('pen' in my_str)

my_list = [0, 2, 4, 6, 8, 10]
print(3 in my_list)

x = None
print(x is None)
print(x is not None)

print('apple' in ['pineapple', 'orange', 'banana'])

print('apple' in 'pineapple')

x = True
y = False
z = None
print(x and z is None)
print(not x or not y)
print(x and not y and z is None)