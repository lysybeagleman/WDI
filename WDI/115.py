from random import randint

def Solve(T, N) -> int:
    max_sum = -float("inf")
    for i in range(N):
        for start in range(N):
            s = 0
            for l in range(10):
                j = start + l
                if j >= N:
                    break
                s += T[i][j]
                if s > max_sum:
                    max_sum = s
    for j in range(N):
        for start in range(N):
            s = 0
            for l in range(10):
                i = start + l
                if i >= N:
                    break
                s += T[i][j]
                if s > max_sum:
                    max_sum = s
    return max_sum         


def main() -> None:
    N = int(input())
    T = [[randint(-10000, 10000) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(Solve(T, N))


main()
