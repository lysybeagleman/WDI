def Spiral(N, T) -> None:
    k = 1 
    up = 0 
    down = N - 1
    left = 0
    right = N - 1
    while k <= N * N:
        for i in range(left, right + 1):
            T[up][i] = k
            k += 1
        up += 1
        for j in range(up, down + 1):
            T[j][right] = k
            k += 1
        right -= 1
        for i in range(right, left - 1, -1):
            T[down][i] = k
            k += 1
        down -= 1
        for j in range(down, up - 1, -1):
            T[j][left] = k
            k += 1
        left += 1


def main() -> None:
    N = int(input())
    T = [[0 for i in range(N)] for j in range(N)]
    Spiral(N, T)
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()


main()
