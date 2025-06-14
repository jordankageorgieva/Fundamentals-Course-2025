numbers = input().split(", ")

positive = [num for num in numbers if int(num) >= 0]
negative = [num for num in numbers if int(num) < 0]
even = [num for num in numbers if int(num) % 2 == 0]
odd = [num for num in numbers if int(num) % 2 != 0]

print("Positive: " + ", ".join(positive))
print("Negative: " + ", ".join(negative))
print("Even: " + ", ".join(even))
print("Odd: " + ", ".join(odd))
