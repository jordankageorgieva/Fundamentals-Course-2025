raw_beggar_data_list = [int(item) for item in input().split(",")]
beggar_count =  int(input())

bagger_result = []
# step for the next bagger in the list
delta = beggar_count

for index in range(beggar_count):
    sum_index = 0
    for data in range(index, len(raw_beggar_data_list), delta):
      # print(f" {index} : {raw_bagger_data_list[data]}")
      sum_index += raw_beggar_data_list[data]

    bagger_result.append(sum_index)


# output
print(bagger_result)