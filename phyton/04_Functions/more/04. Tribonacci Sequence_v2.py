depth_tribonacci = int(input())

def tribonacci_sequence(depth: int):
    if depth <= 0:
        return
    sequence = []

    if depth >= 1:
        sequence.append(1)
    if depth >= 2:
        sequence.append(1)
    if depth >= 3:
        sequence.append(2)

    for index in range(3, depth):
        next_value = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_value)

    print(' '.join(str(num) for num in sequence))

tribonacci_sequence(depth_tribonacci)
