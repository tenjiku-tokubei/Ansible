print('abc')
print('あいう')
print("I'm fine.")
print(type('xyz'))

zen_of_python = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
'''
print(zen_of_python)

my_str = 'この後改行\nしてからタブ\tで空白。'
print(my_str)

# これはコメント行です。
print('a') # ここにも書けます。

print('a')
'''
これは、複数行のコメントです。
a
と
bの間
'''
print('b')
print('abc' + 'xyz')
print('repeat me!' * 3)

print('abc' + str(2))

print(ord('あ'))

print(chr(12354))

answer = '''○●●●
●○●●
●●○●
●●●○
'''
print(answer)

w = '○'
b = '●'
answer = ''
for i in range(4):
    for j in range(4):
        if i == j:
            answer += w
        else:
            answer += b
    answer += '\n'
print(answer)