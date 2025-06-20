sequence = [int(num) for num in input().split(" ")]
average = float(f"{sum(sequence)/len(sequence):.2f}")

sequence_sort = sorted(sequence, reverse=True)
# print(sequence_sort)
# print(average)

greater_than_average = []

if len(sequence_sort) > 5:
    end = 5
else:
    end = len(sequence_sort)

for index in range(0, end):
    if sequence_sort[index] > average:
        greater_than_average.append(sequence_sort[index])

if greater_than_average:
    print(" ".join([str(num) for num in greater_than_average]))
else:
    print("No")