from random import randint

def Solve(T, N) -> tuple[int, int]:
    best_sum = 0
    best_pos = (-1, -1)
    for i in range(N):
        for j in range(N):
            s = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        s += T[ni][nj]
            if s > best_sum:
                best_sum = s
                best_pos = (i, j)
    return best_pos


def main() -> None:
    N = int(input())
    T = [[randint(1, 1000000) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(Solve(T, N))


main()
