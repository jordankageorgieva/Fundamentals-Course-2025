stop = False
legendary_farming ={
    'shards' : 0,
    'fragments' : 0,
    'motes' : 0
}
legendary_item = ''
while not stop:
    line = input().split(" ")
    for index in range(0, len(line), 2):
        quantity = int(line[index])
        item = line[index + 1].lower()
        # print(item)
        if item in legendary_farming.keys():
            legendary_farming[item] += quantity
            if legendary_farming[item] >= 250 and item in ['fragments', 'shards', 'motes']:
                legendary_farming[item] -= 250
                stop = True
                if item == "fragments":
                    legendary_item = 'Valanyr'
                elif item == "shards":
                    legendary_item = 'Shadowmourne'
                elif item == "motes":
                    legendary_item = 'Dragonwrath'
                break
        else:
            # first added junk
            legendary_farming[item] = quantity

print(f"{legendary_item} obtained!")
print("\n".join([key + ": "+ str(value) for key, value in legendary_farming.items()]))
