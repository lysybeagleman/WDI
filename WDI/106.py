from random import randint

def Square(T, N, k) -> None:
    if T[0][0] * T[0][N - 1] * T[N - 1][0] * T[N - 1][N - 1] == k:
        print(f"YES, {N // 2 + 1}, {N // 2 + 1}")
    else:
        for i in range (N, 1, -2):
        


def main() -> None:
    N = int(input())
    k = int(input())
    T = [[randint(1, 8) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    Square(T, N, k)


main()
