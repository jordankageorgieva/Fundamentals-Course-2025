_1_name = input()
_2_name = input()
delimiter = input()

name = [_1_name , _2_name]
name_with_delimiter = delimiter.join(name)

print(name_with_delimiter)
