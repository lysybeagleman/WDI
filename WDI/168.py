from random import randint

def Solve(i, count, sum, R, T) -> int:
    if count == 3:
        return 1 if sum == R else 0
    if i == len(T):
        return 0
    if Solve(i + 1, count + 1, sum + T[i], R, T) == 1:
        return 1
    return Solve(i + 1, count, sum, R, T)


def main() -> None:
    R = int(input())
    N = int(input())
    T = [randint(1, 100) for i in range(N)]
    for i in range(N):
        print(f"{T[i]}", end="")
    print(f"\n{Solve(0, 0, 0, R, T)}")


main()
