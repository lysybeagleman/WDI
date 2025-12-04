from random import randint

def Manhattan(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def First_Digit(n):
    while n > 9:
        n //= 10
    return n


def Solve(T, w, k, cur_dist) -> bool:
    if w == 7 and k == 7:
        return True
    dx = [-1, 0, 1, 1, 1]
    dy = [1, 1, 1, 0, -1]
    for i in range():
        
    


def main() -> None:
    w = int(input())
    k = int(input())
    T = [[randint(1, 1000000) for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            print(f"{T[i][j]}", end="")
        print()
    print("YES" if Solve(T, w, k) else "NO")


main()