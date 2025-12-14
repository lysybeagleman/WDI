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


def Solve(T) -> bool:
    pattern = -1
    for k in range(len(T)):
        count = 0
        for i in range(1, len(T) - 1):
            for j in range(1, len(T) - 1):
                composite = 0
                if T[k][i-1][j] > 1 and not Prime(T[k][i-1][j]):
                    composite += 1
                if T[k][i+1][j] > 1 and not Prime(T[k][i+1][j]):
                    composite += 1
                if T[k][i][j-1] > 1 and not Prime(T[k][i][j-1]):
                    composite += 1
                if T[k][i][j+1] > 1 and not Prime(T[k][i][j+1]):
                    composite += 1
                if composite >= 6:
                    count += 1
        if pattern == -1:
            pattern = count
        elif count != pattern:
            return False
    return True


def main() -> None:
    N = int(input())
    T = [[[randint(1, 10000) for _ in range(N)] for _ in range(N)] for k in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print("YES" if Solve(T, N) else "NO")


main()
