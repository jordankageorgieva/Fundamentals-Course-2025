list_of_strings = input().split()

while True:
    command = input()
    if command == '3:1':
        print(' '.join(list_of_strings))
        break
    parts = command.split()
    if parts[0] == 'merge':
        # start_idx = int(parts[1])
        # end_idx = int(parts[2])
        # fix - clamp the min/max indexes
        start_idx = max(0, min(int(parts[1]), len(list_of_strings) - 1))
        end_idx = max(start_idx, min(int(parts[2]), len(list_of_strings) - 1))
        merged_strs = ''.join(list_of_strings[start_idx:end_idx + 1])
        modified = list_of_strings[:start_idx]
        if modified:
            modified.append(merged_strs)
        else:
            modified = [merged_strs, ]
        modified.extend(list_of_strings[end_idx + 1:])
        list_of_strings = modified
    elif parts[0] == 'divide':
        idx = int(parts[1])
        partitions = int(parts[2])
        text = list_of_strings.pop(idx)
        partition_length = len(text) // partitions
        remainder = len(text) % partitions
        divided = []
        start = 0
        for i in range(partitions):
            if i == partitions - 1:
                divided.append(text[start:])
            else:
                divided.append(text[start:start + partition_length])
                start += partition_length
        for div_idx, div_item in enumerate(divided):
            list_of_strings.insert(idx + div_idx, div_item)