number = int(input())

list_positive = list()
list_negative = list()
for _ in range(number):
    data = int(input())
    if data > 0:
        list_positive.append(data)
    else:
        list_negative.append(data)

print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}")
print(f"Sum of negatives: {sum(list_negative)}")
