from random import randint

def One_Common(a, b) -> bool:
    d = 2
    count = 0
    while d <= a and d <= b:
        if a % d == 0 and b % d == 0:
            count += 1
            while a % d == 0:
                a //= d
            while b % d == 0:
                b //= d
            if count > 1:
                return False
        d += 1
    return count == 1


def Count(T, N, i, j, d) -> int:
    if d == 4:
        return 0
    cnt = 0
    if d == 0:
        if i > 0:
            if One_Common(T[i][j], T[i - 1][j]):
                cnt = 1
    elif d == 1:
        if i < N - 1:
            if One_Common(T[i][j], T[i + 1][j]):
                cnt = 1
    elif d == 2:
        if j > 0:
            if One_Common(T[i][j], T[i][j - 1]):
                cnt = 1
    elif d == 3:
        if j < N - 1:
            if One_Common(T[i][j], T[i][j + 1]):
                cnt = 1
    return cnt + Count(T, N, i, j, d + 1)


def Solve(T, N, i, j) -> int:
    if i == N:
        return 0
    if j == N:
        return Solve(T, N, i + 1, 0)
    cnt = Count(T, N, i, j, 0)
    add = 0
    if cnt == 4:
        add = 1
    return add + Solve(T, N, i, j + 1)


def four(T) -> int:
    return Solve(T, len(T), 0, 0)


def main() -> None:
    N = int(input())
    T = [[randint(1, 1000) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(four(T))


main()
