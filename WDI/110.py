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


def Complementary(n, T, N, n_i, n_j) -> int:
    for i in range(N):
        for j in range(N):
            if not (i == n_i and j == n_j) and Prime(n + T[i][j]):
                return n
    return 0


def Solve(T, N) -> None:
    T_copy = [[T[i][j] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            T[i][j] = Complementary(T[i][j], T_copy, N, i, j)


def main() -> None:
    N = int(input())
    T = [[randint(1, 10000) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    Solve(T, N)
    print("\n")
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()


main()
