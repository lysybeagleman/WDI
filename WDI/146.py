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


def Weight(n) -> int:
    w = 0
    if n % 2 == 0:
        w += 1
    d = 3
    while d * d <= n:
        if n % d == 0 and Prime(d):
            w += 1
        d += 2
    return w


def Partition(i, S, N, T) -> bool:
    if i == N:
        return S[0] == S[1] ==  S[2]
    w = Weight(T[i])
    for j in range(3):
        S[j] += w
        if Partition(i + 1, S, N, T):
            return True
        S[j] -= w
    return False


def Solve(T) -> bool:
    N = len(T)
    S = [0, 0, 0]
    return Partition(0, S, N, T)     


def main() -> None:
    N = int(input())
    T = [randint(1, 1000000) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print()
    print("YES" if Solve(T) else "NO")


main()
