from random import randint

def Check_Non_Parity(n) -> bool:
    while n > 0:
        if n % 10 % 2 == 0:
            return False
        n //= 10
    return True


def Flag(T, N) -> bool:
    counter = 0
    for i in range(N):
        for j in range(N):
            if Check_Non_Parity(T[i][j]):
                counter += 1
                break
    return True if counter == N else False


def main() -> None:
    N = int(input())
    T = [[randint(1, 1000000) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print("YES" if Flag(T, N) else "NO")


main()
