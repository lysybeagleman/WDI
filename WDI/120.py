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


def Condition(a, b) -> bool:
    c = 0
    d = 2
    while d * d <= a and d * d <= b:
        if a % d == 0 and b % d == 0 and Prime(d):
            c += 1
        d += 1
        if c > 1:
            break 
    return c == 1


def four(T) -> int:
    N = len(T)
    res = 0
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if Condition(T[i][j], T[i - 1][j]) and Condition(T[i][j], T[i + 1][j]) and Condition(T[i][j], T[i][j - 1]) and Condition(T[i][j], T[i][j + 1]):
                res += 1
    return res


def main() -> None:
    N = int(input())
    T = [[randint(1, 100) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(four(T))


main()
