from random import randint

def Solve(T, k) -> tuple[bool, tuple[int, int]]:
    for i in range(len(T)):
        for j in range(len(T)):
            d = 1
            while True:
                if i - d < 0 or i + d >= len(T) or j - d < 0 or j + d >= len(T):
                    break
                prod = T[i - d][j - d] * T[i - d][j + d] * T[i + d][j - d] * T[i + d][j + d]
                if prod == k:
                    return True, (i, j)
                d += 1
    return False, None


def main() -> None:
    N = int(input())
    k = int(input())
    T = [[randint(1, 1000000) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    found, center = Solve(T, k)
    print(f"YES, {center}" if found else "NO")


main()
