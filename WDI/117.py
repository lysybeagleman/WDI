from random import randint

def Solve(T, N) -> int:
    knight_moves = [(2, -1), (2, 1), (1, -2), (1, 2)]
    INF = N * N + 1
    dist = [[INF for _ in range(N)] for _ in range(N)]
    for j in range(N):
        if T[0][j] == 0:
            dist[0][j] = 0
    for step in range(N * N):
        updated = False
        for i in range(N):
            for j in range(N):
                if dist[i][j] < INF:
                    for move in knight_moves:
                        ni = i + move[0]
                        nj = j + move[1]
                        if 0 <= ni < N and 0 <= nj < N:
                            if T[ni][nj] == 0 and dist[ni][nj] > dist[i][j] + 1:
                                dist[ni][nj] = dist[i][j] + 1
                                updated = True
        if not updated:
            break
    min_path = INF
    for j in range(N):
        if dist[N - 1][j] < min_path:
            min_path = dist[N - 1][j]
    if min_path == INF:
        return -1
    return min_path


def main() -> None:
    N = int(input())
    T = [[randint(0, 1) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(Solve(T, N))


main()
