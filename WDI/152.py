from random import randint

def Solve(T, i, m) -> bool:
    if m == 0:
        return True
    if i == len(T):
        return False
    if T[i] <= m:
        if Solve(T, i + 1, m - T[i]):
            return True
    return Solve(T, i + 1, m)


def main() -> None:
    N = int(input())
    m = int(input())
    T = [randint(1, 12) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print("\nYES" if Solve(T, 0, m) else "\nNO")


main()
