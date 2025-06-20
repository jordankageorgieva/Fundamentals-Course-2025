
sequence = [element for element in input().split(' ')]
# print(sequence)
integers = input().strip()

moves = 0
while integers != 'end':
    num1, num2 = map(int, integers.split())
    moves += 1
    # print(f"{moves}")
    # print(sequence)
    if ((num1 < 0 or num1 >= len(sequence)) or (num2 < 0 or num2 >= len(sequence))) or (num1 == num2):
    # elif (num1 == num2) or not (0 <= num1 < len(sequence)) or not (0 <= num1 < len(sequence)):
        middle = int(len(sequence) // 2)
        sequence.insert(middle, f'-{moves}a')
        sequence.insert(middle, f'-{moves}a')
        print("Invalid input! Adding additional elements to the board")
        # print(sequence)
    else:
        if sequence[num1] == sequence[num2]:
            element = sequence.pop(max(num1, num2))
            sequence.pop(min(num1, num2))
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    # print(sequence)
    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break
    integers = input()

if sequence:
    print("Sorry you lose :(")
    print(" ".join(sequence))