from random import randint

def Solve(T, sum_val, sum_idx, i, count) -> int:
    if sum_val == sum_idx and count > 0:
        return (count, sum_val)
    if i == len(T):
        return None
    res1 = Solve(T, sum_val, sum_idx, i + 1, count)
    res2 = Solve(T, sum_val + T[i], sum_idx + i, i + 1, count + 1)
    if res1 is None:
        return res2
    if res2 is None:
        return res1
    return res1[1] if res1[0] < res2[0] else res2[1]


def main() -> None:
    N = int(input())
    T = [randint(1, 10) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print()
    print(Solve(T, 0, 0, 0, 0))


main()
