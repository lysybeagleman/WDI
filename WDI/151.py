def TwoThreeFive(n) -> bool:
    if n == 1:
        return True
    for p in [2, 3, 5]:
        if n % p == 0:
            return TwoThreeFive(n // p)
    return False


def Solve(i, N) -> None:
    if i > N:
        return
    if TwoThreeFive(i):
        print(i, end=" ")
    Solve(i + 1, N)


def main() -> None:
    N = int(input())
    Solve(1, N)


main()
