with open('sample.txt', 'r') as f:
    for line in f:
        print(line.strip())

with open('sample.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

with open('sample.txt', 'r') as f:
    lines = list(f)
    print(lines)

with open('sample.txt', 'r+') as f:
    line = f.readline()
    print(line)

with open('number.txt', 'r') as f:
    sum = 0
    for data in f:
        num = int(data)
        sum += num
    print(sum)