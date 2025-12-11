def Solve(n, f1, f2) -> int:
    if n == 1:
        return f1
    return Solve(n - 1, f2, f1 + f2)


def main() -> None:
    n = int(input())
    print(Solve(n, 1, 1))


main()
