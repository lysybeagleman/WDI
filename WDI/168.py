from random import randint

def Solve() -> int:
    


def main() -> None:
    N = int(input())
    T = [randint(1, 100) for i in range(N)]
    for i in range(N):
        print(f"{T[i]}", end="")
    print(f"\n{Solve()}")


main()
