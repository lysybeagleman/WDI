from random import randint

def distance(T) -> int:
    N = len(T)
    arr = [0 for i in range(N)]
    for i in range(N):
        d = 0
        for j in range(N):
            d = d * 2 + T[i][j]
        arr[i] = d
    max_val = arr[0]
    min_val = arr[0]
    for i in range(1, N):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
    return max_val - min_val


def main() -> None:
    N = int(input())
    T = [[randint(0, 1) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(distance(T))


main()
