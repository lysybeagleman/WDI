def Solve(n, max_n, arr, k) -> None:
    if n == 0:
        for i in range(k):
            if i > 0:
                print("+", end="")
            print(arr[i], end="")
        print()
    for i in range(1, max_n + 1):
        if i < n:
            arr[i] = i
            Solve(n - i, i, arr, i + 1)


def main():
    n = int(input())
    arr = [0 for i in range(n)]
    Solve(n, n, arr, 0)


main()
