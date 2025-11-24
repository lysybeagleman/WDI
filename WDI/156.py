from random import randint

def Solve(T, N, target, i, current_product) -> int:
    if i == N:
        if current_product == target:
            return 1
        else:
            return 0
    count_with = 0
    if current_product * T[i] <= target and target % (current_product * T[i]) == 0:
        count_with = Solve(T, N, target, i + 1, current_product * T[i])
    count_without = Solve(T, N, target, i + 1, current_product)
    return count_with + count_without


def main() -> None:
    N = int(input())
    target = int(input())
    T = [randint(1, 100) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    print()
    print(Solve(T, N, target, 0, 1))


main()
