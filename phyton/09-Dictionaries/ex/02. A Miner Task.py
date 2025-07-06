resource = input()
miner = {}
while resource != 'stop':
    quantity = int(input())
    if resource not in miner.keys():
        miner[resource] = 0
    miner[resource] += quantity
    resource = input()
print(miner)
print("\n".join([key + " -> "+ str(value) for key, value in miner.items()]))
