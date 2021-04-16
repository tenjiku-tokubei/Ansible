import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ch = random.choice(alphabet)
while True:
    val = input()
    if ch == val:
        print('OK')
        break
    else:
        print('NG')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sample4 = random.sample(numbers, k=4)
num4 = ''.join(sample4)
while True:
    val = input()
    if val == num4:
        print('OK')
        break
    else:
        print(val, ': NG')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num4 = ''.join(random.sample(numbers, k=4))
while True:
    val = input()
    if val == num4:
        break
    if len(val) != 4:
        print('input 4 numbers.')
        continue
    answer = ''
    for i in range(4):
        if num4[i] == val[i]:
            answer += num4[i]
        else:
            answer += 'X'
    print('->' + answer)

