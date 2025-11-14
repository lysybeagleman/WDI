from random import randint

def Cost(t, k, w) -> int:
    if k < 0 or k > 7:
        return float("inf")
    if w == 7:
        return t[w][k]
    min_cost = t[w][k]
    c1 = Cost(t, k - 1, w + 1)
    c2 = Cost(t, k, w + 1)
    c3 = Cost(t, k + 1, w + 1)
    if c1 < min_cost:
        min_cost = c1
    if c2 < min_cost:
        min_cost = c2
    if c3 < min_cost:
        min_cost = c3
    return t[w][k] + min_cost


def main() -> None:
    k = int(input())
    t = [[randint(1, 10) for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            print(f"{t[i][j]} ", end="")
        print()
    print(Cost(t, k, 0))


main()
