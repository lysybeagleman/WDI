from math import sqrt
from random import randint

def Field(x1, x2) -> int:
    return (x2 - x1) ** 2


def Overlap(A, B) -> bool:
    x1a, x2a, y1a, y2a = A
    x1b, x2b, y1b, y2b = B
    if x2a <= x1b or x2b <= x1a:
        return False
    if y2a <= y1b or y2b <= y1a:
        return False
    return True


def Solve(T, field_sum, i, counter, used) -> bool:
    if i == len(T) and (field_sum != 2012 or counter != 13):
        return False
    if Solve(T, field_sum, i + 1, counter, used):
        return True
    for j in range(len(T)):
        if used[j] == 1:
            if Overlap(T[j], T[i]):
                return False
    new_used = [0 for _ in range(len(T))]
    for k in range(len(T)):
        new_used[k] = used[k]
    new_used[i] = 1
    pole = Field(T[i][0], T[i][1])
    if field_sum + pole <= 2012 and counter + 1 <= 13:
        if Solve(T, field_sum + pole, i + 1, counter + 1, new_used):
            return True
    return False


def main() -> None:
    N = int(input())
    T = []
    for i in range(N):
        dist = randint(1, 200)
        x1 = randint(1, 100)
        y1 = randint(1, 100)
        T.append((x1, x1 + dist, y1, y1 + dist))
    for coord in T:
        print(coord[0], coord[1], coord[2], coord[3])
    print("YES" if Solve(T, Field(T[0][0], T[0][1]), 0, 0, [0 for i in range(N)]) else "NO")


main()
