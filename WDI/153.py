from random import randint

def Solve(T, i, diff, m) -> bool:
    n = len(T)
    if i == n:
        return diff == m
    if Solve(T, i + 1, diff + T[i], m):
        return True
    if Solve(T, i + 1, diff - T[i], m):
        return True
    return Solve(T, i + 1, diff, m)


def main() -> None:
    N = int(input())
    m = int(input())
    T = [randint(1, 12) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print("\nYES" if Solve(T, 0, 0, m) else "\nNO")


main()
