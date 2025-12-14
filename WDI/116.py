from random import randint

def Solve(T, N, prod) -> int:
    c = 0
    for i in range(N):
        for j in range(N):
            if i + 2 < N and j + 1 < N:
                if T[i][j] * T[i + 2][j + 1] == prod:
                    c += 1
            if i + 2 < N and j - 1 >= 0:
                if T[i][j] * T[i + 2][j - 1] == prod:
                    c += 1
            if i - 2 >= 0 and j + 1 < N:
                if T[i][j] * T[i - 2][j + 1] == prod:
                    c += 1
            if i - 2 >= 0 and j - 1 >= 0:
                if T[i][j] * T[i - 2][j - 1] == prod:
                    c += 1
            if i + 1 < N and j + 2 < N:
                if T[i][j] * T[i + 1][j + 2] == prod:
                    c += 1
            if i - 1 >= 0 and j + 2 < N:
                if T[i][j] * T[i - 1][j + 2] == prod:
                    c += 1
            if i + 1 < N and j - 2 >= 0:
                if T[i][j] * T[i + 1][j - 2] == prod:
                    c += 1
            if i - 1 >= 0 and j - 2 >= 0:
                if T[i][j] * T[i - 1][j - 2] == prod:
                    c += 1
    return c // 2


def main() -> None:
    N = int(input())
    prod = int(input())
    T = [[randint(1, 10000) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(Solve(T, N, prod))


main()
