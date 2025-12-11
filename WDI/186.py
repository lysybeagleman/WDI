from random import randint

def SolveRec(T, N, i, target, a, d) -> bool:
    if i == N:
        return True
    s = 0
    for j in range(i, N):
        s += T[j]
        if s == target:
            if SolveRec(T, N, j + 1, target + d, a, d):
                return True
    return False


def Solve(T, N):
    s1 = 0
    for i in range(N):
        s1 += T[i]
        a = s1
        s2 = 0
        for j in range(i + 1, N):
            s2 += T[j]
            d = s2 - a
            if d > 0:
                if SolveRec(T, N, j + 1, a + 2 * d, a, d):
                    print("\n", a, d)
                    return (a, d)
    return None


def sequence(T):
    return Solve(T, len(T))


def main() -> None:
    N = int(input())
    T = [randint(1, 100) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    sequence(T)


main()
