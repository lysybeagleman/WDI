from random import randint

def Result(T, N) -> tuple[int, int]:
    max_i_j = tuple()
    max_ratio = 0
    sums_i = [0 for i in range(N)]
    sums_j = [0 for j in range(N)]
    for i in range(N):
        sum_i = 0
        for j in range(N):
            sum_i += T[i][j]
        sums_i[i] = sum_i
    for j in range(N):
        sum_j = 0
        for i in range(N):
            sum_j += T[i][j]
        sums_j[j] = sum_j
    for i in range(N):
        for j in range(N):
            if sums_j[j] / sums_i[i] > max_ratio:
                max_ratio = sums_j[j] / sums_i[i]
                max_i_j = (i + 1, j + 1)
    return max_i_j
    

def main() -> None:
    N = int(input())
    T = [[randint(1, 1000000) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(Result(T, N))


main()
