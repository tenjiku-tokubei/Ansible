print(pow(2, 3))
print(pow(3, 2))
print(2, 3, 4)
print(4, 3, 2)

print(2, 3, 4, sep='/')

print(2, 3, 4, sep='/', end='---\n')
print(2, 3, 4, end='---\n', sep='/')

args_vals = [2, 3, 4]
print(*args_vals)
print(args_vals)

print(pow(*divmod(20, 3)))

result = divmod(20, 3)
print(result[0], result[1])

sample_list = [2, 3, 4]
print(list(map(str, sample_list)))

print(list(map(int, '123')))