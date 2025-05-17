event = input()

n_coffee = 0
while event != "END":

    if event.lower() in ["coding", "dog", "cat", "movie"]:
        if event.islower():
            n_coffee += 1
        elif event.isupper():
            n_coffee += 2
    # print(event + " - "  + str(n_coffee))
    event = input()

if n_coffee <= 5:
    print(n_coffee)
else:
    print("You need extra sleep")