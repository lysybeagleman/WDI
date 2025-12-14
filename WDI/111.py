from random import randint

def Ones(n) -> int:
    c = 0
    while n > 0:
        if n % 2 == 1:
            c += 1
        n //= 2
    return c


def Solve(T1, T2) -> bool:
    N1 = len(T1)
    N2 = len(T2)
    for i_shift in range(N2 - N1 + 1):
        for j_shift in range(N2 - N1 + 1):
            count = 0
            for i in range(N1):
                for j in range(N1):
                    if Ones(T1[i][j]) == Ones(T2[i_shift + i][j_shift + j]):
                        count += 1
            if count * 100 > N1 * N1 * 33:
                return True
    return False


def main() -> None:
    N1 = int(input())
    N2 = int(input())
    T1 = [[randint(1, 10000) for _ in range(N1)] for _ in range(N1)]
    T2 = [[randint(1, 10000) for _ in range(N2)] for _ in range(N2)]
    for i in range(N1):
        for j in range(N1):
            print(f"{T1[i][j]} ", end="")
        print()
    print("\n")
    for i in range(N2):
        for j in range(N2):
            print(f"{T2[i][j]} ", end="")
        print()
    print("\nYES" if Solve(T1, T2) else "NO")


main()
