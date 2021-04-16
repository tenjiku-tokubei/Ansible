a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

a, b = b, a
print(a)
print(b)

d = (1, 2)
e, f = d
print(e)
print(f)

x = [10, 30]
y, z = x
print(x)
print(y)

p = (1, (10, 100))
q, (r, s) = p
print(q)
print(r)
print(s)

a, b, c = 1, 2.3, 'mojiretsu'
print(a)
print(b)
print(c)

a, b, c, d = 1, 2, 3, 4
a, b, c, d = c, d, a, b
print(a)

a = 1
b = 2
a, b = b, a + b
a, b = b, a + b
print(a)
