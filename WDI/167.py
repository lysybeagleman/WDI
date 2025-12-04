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


def Solve(T, V, i, steps, N) -> int:
    if i == N - 1:
        return steps
    V[i] = 1
    factors = [0 for _ in range(T[i])]
    k = 0
    d = 2
    while d < T[i]:
        if T[i] % d == 0:
            if Prime(d):
                factors[k] = i
                k += 1
        d += 1
    j = 0
    while j < len(factors):
        k = factors[j]
        if k == 0:
            break
        ni = i + k
        if ni < N and V[ni] == 0:
            res = Solve(T, V, ni, steps + 1, N)
            if res != -1:
                return res
        j += 1
    return -1


def main() -> None:
    N = int(input())
    T = [randint(1, 1000000) for i in range(N)]
    for i in range(N):
        print(f"{T[i]}", end="")
    print(f"\n{Solve(T, [0 for i in range(N)], 0, 0, N)}")


main()
