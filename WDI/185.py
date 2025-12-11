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


def Solve(T, N, i, s0, s1) -> bool:
    if i == N:
        return (s0 == s1)
    arr = [0 for _ in range(5)]
    cnt = 0
    for d in range(-2, 3):
        v = T[i] + d
        if v >= 2 and Prime(v):
            arr[cnt] = v
            cnt += 1
    if cnt == 0:
        return False
    for k in range(cnt):
        v = arr[k]
        if Solve(T, N, i + 1, s0, s1 + v):
            return True
    return False


def gold(T) -> bool:
    N = len(T)
    s0 = 0
    for i in range(N):
        s0 += T[i]
    return Solve(T, N, 0, s0, 0)


def main() -> None:
    N = int(input())
    T = [randint(1, 100) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print("\nYES" if gold(T) else "\nNO")


main()
