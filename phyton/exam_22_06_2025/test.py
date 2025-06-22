import  math
students = int(input())

# print(math.ceil(students * 0.8))

free_flour = students // 5
all_flour = free_flour * 4 + students % 5

print(free_flour)
print(all_flour)