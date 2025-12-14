from random import randint

def Solve(T, N) -> bool:
    for i in range(N):
        found = False
        for j in range(N):
            if T[i][j] == 0:
                found = True
                break
        if not found:
            return False
    for j in range(N):
        found = False
        for i in range(N):
            if T[i][j] == 0:
                found = True
                break
        if not found:
            return False
    return True


def main() -> None:
    N = int(input())
    T = [[randint(0, 5) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    print(f"YES, " if Solve(T, N) else "NO")


main()
