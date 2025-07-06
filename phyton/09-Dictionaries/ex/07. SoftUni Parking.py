n = int(input())
parking= {}
for _ in range(n):
    command = input().split(" ")
    name = command[1]
    if command[0] == "register":
        car = command[2]
        if name in parking.keys():
            print(f"ERROR: already registered with plate number {car}")
        else:
            parking[name] = car
            print(f"{name} registered {car} successfully")
    elif command[0] == "unregister":
        if name not in parking.keys():
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            # del parking[command[1]]
            print(f"{name} unregistered successfully")


print("\n".join([key + " => "+ str(value) for key, value in parking.items()]))
