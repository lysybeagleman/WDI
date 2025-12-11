from math import sqrt

def Prime(n) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def Solve(pos, ones_left, current) -> int:
    if ones_left < 0:
        return 0
    remaining_positions = pos + 1
    if ones_left > remaining_positions:
        return 0
    if ones_left == 0:
        if Prime(current):
            return 0
        else:
            return 1
    if ones_left == remaining_positions:
        added = (1 << (pos + 1)) - 1
        final_value = current + added
        if Prime(final_value):
           return 0
        else:
            return 1
    val_with_one = current + (1 << pos)
    cnt1 = Solve(pos - 1, ones_left - 1, val_with_one)
    cnt2 = Solve(pos - 1, ones_left, current)
    return cnt1 + cnt2


def main() -> None:
    A = int(input())
    B = int(input())
    print(0 if A <= 0 or B <= 0 else Solve(A + B - 2, A - 1, 1 << (A + B - 1)))


main()
