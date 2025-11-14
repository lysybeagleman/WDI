from random import randint

def Order(T1, N, M, T2) -> None:
    TMP = [0 for i in range(M)]
    k = 0
    for j in range(N):
        for i in range(N):
            TMP[k] = T1[i][j]
            k += 1
    for i in range(M - 1):
        for j in range(M - i - 1):
            if TMP[j] >= TMP[j + 1]:
                tmp = TMP[j]
                TMP[j] = TMP[j + 1]
                TMP[j + 1] = tmp
    k = 0
    for i in range(M - 1, -1, -1):
        if TMP[i] != 0:
            T2[k] = TMP[i]
            k += 1
    

def main() -> None:
    N = int(input())
    M = N * N
    T1 = [list(sorted([randint(-1000000, 1000000) for i in range(N)], reverse=True)) for j in range(N)]
    T2 = [0 for i in range(M)]
    for i in range(N):
        for j in range(N):
            print(f"{T1[i][j]} ", end="")
        print()
    Order(T1, N, M, T2)
    for i in range(M):
        print(f"{T2[i]} ", end="")


main()
