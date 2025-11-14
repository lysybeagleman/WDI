def Newton(n, k) -> int:
    if k == 0 or k == n:
        return 1
    if k == 1 or k == n - 1:
        return n
    return Newton(n - 1, k - 1) + Newton(n - 1, k)


def main():
    n = int(input())
    k = int(input())
    print(Newton(n, k))

main()
