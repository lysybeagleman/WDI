from random import randint

def Find(T, N) -> None:
    found = False
    max_len = 2
    for i in range(N):
        for j in range(N):
            k = i
            m = j
            cur_len = 2
            while k > 2 and m < N - 2:
                if T[k][m] != 1 and T[k - 1][m + 1] != 1 and T[k][m] / T[k - 1][m + 1] == T[k - 1][m + 1] / T[k - 2][m + 2]:
                    found = True
                    cur_len += 1
                    if cur_len > max_len:
                        max_len = cur_len
                else:
                    break
                k -= 1
                m += 1
    print(f"YES, max length = {max_len}" if found else "NO")

    

def main() -> None:
    N = int(input())
    T = [[randint(1, 1000000) for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            print(f"{T[i][j]} ", end="")
        print()
    Find(T, N)


main()
