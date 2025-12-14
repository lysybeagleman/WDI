from random import randint

def Digits(n, D) -> None:
    while n > 0:
        D[n % 10] = True
        n //= 10


def Friendly(Da, b) -> bool:
    Db = [False for i in range(10)]
    Digits(b, Db)
    for i in range(10):
        if Da[i] != Db[i]:
            return False
    return True


def Solve(T, N) -> int:
    c = 0
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            Da = [False for i in range(10)]
            Digits(T[i][j], Da)
            if Friendly(Da, T[i - 1][j - 1]) and Friendly(Da, T[i - 1][j]) and Friendly(Da, T[i - 1][j + 1]) and Friendly(Da, T[i][j - 1]) and Friendly(Da, T[i][j + 1]) and Friendly(Da, T[i + 1][j - 1]) and Friendly(Da, T[i + 1][j]) and Friendly(Da, T[i + 1][j + 1]):
                c += 1
    return c


def main() -> None:
    N = int(input())
    T = [[randint(1, 10000) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(Solve(T, N))


main()
