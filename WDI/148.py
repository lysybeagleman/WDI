def Jump() -> None:

def main() -> None:
    k = int(input())
    t = [[randint(1, 10) for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            print(f"{t[i][j]} ", end="")
        print()
    print(Cost(t, k, 0))


main()
