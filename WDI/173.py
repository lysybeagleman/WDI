from random import uniform

def DFS(idx, k, sx, sy, sz, T, N, r) -> bool:
        if k >= 3:
            if sx * sx + sy * sy + sz * sz <= k * k * r:
                return True
        if idx == N:
            return False
        x, y, z = T[idx]
        if DFS(idx + 1, k + 1, sx + x, sy + y, sz + z, T, N, r):
            return True
        if DFS(idx + 1, k, sx, sy, sz, T, N, r):
            return True
        return False


def Solve(T, r) -> bool:
    return DFS(0, 0, 0.0, 0.0, 0.0, T, len(T), r * r)


def main() -> None:
    N = int(input())
    r = float(input())
    T = [(uniform(1, 100), uniform(1, 100), uniform(1, 100)) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print("\nYES" if Solve(T, r) else "\nNO")


main()
