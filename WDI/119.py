from random import randint

def chess(T) -> tuple[int, int, int, int]:
    N = len(T)
    row_sum = [0 for _ in range(N)]
    col_sum = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            row_sum[i] += T[i][j]
            col_sum[j] += T[i][j]
    max_sum = -float("inf")
    best_pos = (0, 0, 0, 0)
    for r1 in range(N):
        for c1 in range(N):
            sum1 = row_sum[r1] + col_sum[c1] - T[r1][c1]
            for r2 in range(N):
                for c2 in range(N):
                    if r1 == r2 and c1 == c2:
                        continue
                    sum2 = row_sum[r2] + col_sum[c2] - T[r2][c2]
                    overlap = 0
                    if r1 == r2:
                        overlap += T[r1][c2]
                    if c1 == c2:
                        overlap += T[r2][c1]
                    total = sum1 + sum2 - overlap
                    if total > max_sum:
                        max_sum = total
                        best_pos = (r1, c1, r2, c2)
    return best_pos


def main() -> None:
    N = int(input())
    T = [[randint(-100, 100) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(chess(T))


main()
