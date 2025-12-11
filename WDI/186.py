from random import randint

def Solve(T, N):



def sequence(T):
    return Solve(T, len(T))


def main() -> None:
    N = int(input())
    T = [randint(1, 100) for i in range(N)]
    for i in range(N):
        print(f"{T[i]} ", end="")
    sequence(T)


main()
