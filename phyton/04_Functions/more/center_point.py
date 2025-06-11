import math

X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())


def distance_from_center(x: int, y: int) -> int:
    return math.sqrt(x * x + y * y)

def closer_to_center_point(c1: int, c2: int) -> bool:
    isC1closerPoint: bool = False
    if C1.real < C2.real:
        return isC1closerPoint
    return isC1closerPoint

C1 = distance_from_center(X1, Y1)
C2 = distance_from_center(X2, Y2)

if C2.real < C1.real:
    print(f"({math.floor(X2)}, {math.floor(Y2)})")
else:
    print(f"({math.floor(X1)}, {math.floor(Y1)})")
