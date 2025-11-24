from random import randint

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


def Decimal(T, i, j) -> int:
    d = 0
    for i in range(i, j):
        d = d * 2 + T[i]
    return d


def Solve(T, i) -> bool:
    N = len(T)
    if i == N:
        return True
    min = 30
    if N - i < min:
        min = N - i
    for length in range(1, min + 1):
        if Prime(Decimal(T, i, i + length)):
            if Solve(T, i + length):
                return True
    return False


def main() -> None:
    N = int(input())
    T = [randint(0, 1) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print()
    print("YES" if Solve(T, 0) else "NO")


main()
