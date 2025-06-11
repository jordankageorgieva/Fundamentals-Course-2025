# from center_point import distance_from_center, closer_to_center_point
# point 1
import math

X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())
# point 2
X3 = float(input())
Y3 = float(input())
X4 = float(input())
Y4 = float(input())

def distance_from_center(x: int, y: int) -> float:
    return math.sqrt(x**2 + y**2)

C1 = distance_from_center(X1 - X2, Y1 - Y2)

C2 = distance_from_center(X3 - X4, Y3 - Y4)

if C1 > C2:
    internal_1 = distance_from_center(X1, Y1)
    internal_2 = distance_from_center(X2, Y2)
    if internal_1 > internal_2:
        print(f"({math.floor(X2)}, {math.floor(Y2)})({math.floor(X1)}, {math.floor(Y1)})")
    else:
        print(f"({math.floor(X1)}, {math.floor(Y1)})({math.floor(X2)}, {math.floor(Y2)})")
else:
    internal_1 = distance_from_center(X3, Y3)
    internal_2 = distance_from_center(X4, Y4)
    if internal_1 > internal_2:
        print(f"({math.floor(X4)}, {math.floor(Y4)})({math.floor(X3)}, {math.floor(Y3)})")
    else:
        print(f"({math.floor(X3)}, {math.floor(Y3)})({math.floor(X4)}, {math.floor(Y4)})")

