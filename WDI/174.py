from random import uniform

def DFS(idx, n, sx, sy, T, N, r, k) -> bool:
    if n >= 1 and n < k and n % 3 == 0:
        if sx * sx + sy * sy < n * n * r:
            return True
    if idx == N:
        return False
    x, y = T[idx]
    if DFS(idx + 1, n + 1, sx + x, sy + y, T, N, r, k):
        return True
    if DFS(idx + 1, n, sx, sy, T, N, r, k):
        return True
    return False


def Solve(T, r, k) -> bool:
    return DFS(0, 0, 0.0, 0.0, T, len(T), r * r, k)


def main() -> None:
    N = int(input())
    r = float(input())
    k = float(input())
    T = [(uniform(1, 100), uniform(1, 100)) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print("\nYES" if Solve(T, r, k) else "\nNO")


main()
