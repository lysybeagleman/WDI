from random import randint

def det(A) -> float:
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    wynik = 0.0
    for k in range(n):
        B = [[A[i][j] for j in range(n) if j != k] for i in range(1, n)]
        if (k % 2) == 0:
            wynik += A[0][k] * det(B)
        else:
            wynik -= A[0][k] * det(B)
    return wynik


def main() -> None:
    n = int(input())
    A = [[randint(1, 10) for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            print(f"{A[i][j]} ", end="")
        print()
    print(det(A))


main()
