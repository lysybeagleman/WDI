from random import randint

def Solve(T, min_sum, min_i_sum, i) -> int:
    if min_sum == min_i_sum and min_i_sum > 0:
        return min_sum
    if i == len(T):
        return 0
    res_1 = Solve(T, min_sum, min_i_sum, i + 1)
    res_2 = Solve(T, min_sum + T[i], min_i_sum + i, i + 1)
    if res_1 > 0:
        return res_1
    return res_2


def main():
    N = int(input())
    T = [randint(1, 10) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print()
    print(Solve(T, 0, 0, 0))


main()
