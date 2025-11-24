def Jump(T, N, x, y, move, dx, dy) -> bool:
    T[x][y] = move
    if move == N * N:
        return True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and T[x][y] == 0:
            if Jump(nx, ny, move + 1):
                return True
    T[x][y] = 0
    return False


def main() -> None:
    N = int(input())
    T = [[0 for i in range(N)] for j in range(N)]
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    Jump(T, N, 0, 0, 1, dx, dy)
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()


main()
