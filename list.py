print([2, 4, 8, 16] + [3, 6, 9, 12])

my_list = [2, 4, 8, 16]
my_list + [3, 6, 9, 12]
print(my_list)

my_list = [2, 4, 8, 16]
my_list.append(3)
my_list.append(6)
my_list.append(9)
print(my_list)

my_list = [2, 4, 8, 16]
my_list.extend([3, 6, 9, 12])
print(my_list)

my_list = [2, 4, 8, 16]
my_list.extend([3, 6, 9, 12])
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
my_list.sort()
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
my_list.sort(reverse=True)
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
my_list.reverse()
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
my_list.sort()
my_list.reverse()
print(my_list)

my_list = [2, 4, 8, 16, 3, 6, 9, 12]
new_list = sorted(my_list)
rev_list = sorted(my_list, reverse=True)
print(my_list)
print(new_list)
print(rev_list)

my_list = []
my_list.append('orange')
my_list.append('apple')
my_list.append('grape')
my_list.append('banana')
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse = True)
print(my_list)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[2])
print(my_list[-1])
print(my_list[2:7])
print(my_list[2:7:2])
print(my_list[6:1:-1])
print(my_list[:])
print(my_list[::-1])
print(my_list[6:100])
print(my_list[50:100])
print(my_list[:3])
print(my_list[4:])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
my_list[0] = -1
print(my_list)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
my_list[2:4] = [102, 103]
print(my_list)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
my_list[2:4] = [101, 102, 103, 104]
print(my_list)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
my_list[2:2] = [101, 102]
print(my_list)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
my_list[2:6] = [101, 102]
print(my_list)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
my_list[2:6] = []
print(my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_even = my_list[::-2]
print(reverse_even)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
reverse_even = my_list[-2::-2]
print(reverse_even)

my_list = ['I', 'have', 'an', 'apple']
my_list[2:4] = ['a', 'pineapple']
print(my_list)