from random import randint

def Solve(T, i, diff, m, arr) -> bool:
    n = len(T)
    if i == n:
        return diff == m
    arr[i] = T[i]
    if Solve(T, i + 1, diff + T[i], m, arr):
        return True
    arr[i] = -T[i]
    if Solve(T, i + 1, diff - T[i], m, arr):
        return True
    arr[i] = 0
    return Solve(T, i + 1, diff, m, arr)


def main() -> None:
    N = int(input())
    m = int(input())
    T = [randint(1, 12) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    arr = [0 for i in range(N)]
    ok = Solve(T, 0, 0, m, arr)
    if ok:
        for i in range(N):
            if arr[i] != 0:
                print(f"{arr[i]} ", end="")
    else:
        print("Can't weigh")


main()
