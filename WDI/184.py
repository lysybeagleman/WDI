def A(x) -> int:
    r = 0
    t = x
    while t > 0:
        r = r*10 + (t % 10)
        t //= 10
    return r + 1


def Prime(n) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def B(x) -> int:
    y = x + 1
    while not Prime(y):
        y += 1
    return y


def C(x) -> int:
    y = 10
    while y // x == 0:
        y *= 10
    res = 0
    for _ in range(3):
        d = y // x
        res = res * 10 + d
        y = (y - d * x) * 10
    return res


def DFS(v, depth, seq, best, x) -> str:
    if depth >= 10:
        return
    if depth > 0 and v == x:
        if best[0] is None or len(seq) < len(best[0]):
            best[0] = seq
        return
    DFS(A(v), depth + 1, seq + "A", best, x)
    DFS(B(v), depth + 1, seq + "B", best, x)
    DFS(C(v), depth + 1, seq + "C", best, x)


def cykl(x) -> str:
    best = [None]
    DFS(x, 0, "", best, x)
    return best[0] if best[0] is not None else ""


def main():
    x = int(input())
    print(cykl(x))


main()