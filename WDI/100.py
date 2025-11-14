from random import randint

def Check_Parity(n) -> bool:
    while n > 0:
        if n % 10 % 2 == 0:
            return True
        n //= 10
    return False


def Flag(T, N) -> bool:
    for i in range(N):
        flag = True
        for j in range(N):
            if not Check_Parity(T[i][j]):
                flag = False
                break
        if flag:
            return True
    return False


def main() -> None:
    N = int(input())
    T = [[randint(1, 1000000) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print("YES" if Flag(T, N) else "NO")


main()
