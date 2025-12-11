from random import randint

def Sum(T) -> int:
    S = 0
    for i in range(len(T)):
        S += T[i]
    return S


def Bit_Count(n) -> int:
    c = 0
    while n > 0:
        if n % 2 == 1:
            c += 1
        n //= 2
    return c


def DFS(i, sA, sB, sC, ones, target, N) -> bool:
        if i == N:
            return (sA == sB == sC == target)
        x = ones[i]
        if sA + x <= target:
            if DFS(i + 1, sA + x, sB, sC, ones, target, N):
                return True
        if sB + x <= target:
            if DFS(i + 1, sA, sB + x, sC, ones, target, N):
                return True
        if sC + x <= target:
            if DFS(i + 1, sA, sB, sC + x, ones, target, N):
                return True
        return False


def Solve(T, N) -> bool:
    ones = [0] * N
    for i in range(N):
        ones[i] = Bit_Count(T[i])
    total = Sum(ones)
    if total % 3 != 0:
        return False
    target = total // 3
    return DFS(0, 0, 0, 0, ones, target, N)


def main() -> None:
    N = int(input())
    T = [randint(1, 100) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print("\nYES" if Solve(T, N) else "\nNO")


main()
