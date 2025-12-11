def Prime(n) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def Pow_10(n):
    p = 1
    for i in range(n):
        p *= 10
    return p


def Digits(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c


def Solve(N, pieces) -> bool:
    if N == 0:
        return Prime(pieces)
    total_digits = Digits(N)
    k = 1
    while k <= total_digits:
        p10 = Pow_10(k)
        part = N % p10
        rest = N // p10
        if Prime(part):
            if Solve(rest, pieces + 1):
                return True
        k += 1
    return False


def main() -> None:
    N = int(input())
    print("YES" if Solve(N, 0) else "NO")


main()
