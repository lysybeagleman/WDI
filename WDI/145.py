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


def DigitCount(n) -> int:
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c


def Solve(n) -> None:
    if n > 9 and Prime(n):
        print(f"{n} ", end="")
    k = DigitCount(n)
    for i in range(k):
        p = 1
        j = 0
        while j < i:
            p *= 10
            j += 1
        l = n // (p * 10)
        r = n % p
        d = l * p + r
        if d > 9:
            Solve(d)
        i += 1


def main() -> None:
    n = int(input())
    Solve(n)


main()
