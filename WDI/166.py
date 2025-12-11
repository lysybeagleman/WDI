from random import randint

def Sum(T):
    s = 0
    for i in range(len(T)):
        s += T[i]
    return s


def Solve(T, S, k, w) -> bool:
    if k == None:
        k = [1 for i in range(8)]
        w = [1 for i in range(8)]
    if S == 0:
        return True
    if S < 0 or Sum(k) == 0:
        return False
    for i in range(8):
        for j in range(8):
            if w[i] == 1 and k[i] == 1:
                w[i] = 0
                k[j] = 0
                if Solve(T, S - T[i][j], k, w):
                    return True
                w[i] = 1
                k[j] = 1



def main() -> None:
    S = int(input())
    T = [[randint(1, 100) for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            print(f"{T[i][j]}", end="")
        print()
    print("YES" if Solve(T, S, None, None) else "NO")


main()
