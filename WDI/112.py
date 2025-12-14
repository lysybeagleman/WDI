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


def Digit(n) -> bool:
    while n > 0:
        if Prime(n % 10):
            return True
        n //= 10
    return False


def Solve(T, N) -> bool:
    for i in range(N):
        ok = True
        for j in range(N):
            if not Digit(T[i][j]):
                ok = False
                break
        if ok:
            return True
    return False


def main() -> None:
    N = int(input())
    T = [[randint(1, 10000) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print("YES" if Solve(T, N) else "NO")


main()
