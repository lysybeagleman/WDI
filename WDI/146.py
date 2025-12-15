from random import randint

def Weight(n) -> int:
    d = 2
    w = 0
    while d * d <= n:
        if n % d == 0:
            w += 1
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        w += 1
    return w


def Partition(i, S, N, T) -> bool:
    if N < 3:
        return False
    if i == N:
        return S[0] == S[1] == S[2]
    w = Weight(T[i])
    for j in range(3):
        S[j] += w
        if Partition(i + 1, S, N, T):
            return True
        S[j] -= w
    return False


def Solve(T) -> bool:
    return Partition(0, [0, 0, 0], len(T), T)     


def main() -> None:
    N = int(input())
    T = [randint(1, 1000000) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print()
    print("YES" if Solve(T) else "NO")


main()
