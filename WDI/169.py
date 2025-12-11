from math import sqrt

def Solve(T, i, sumAx, sumAy, cntA, sumBx, sumBy, cntB, best) -> float:
    if i == len(T):
        if cntA > 0 and cntB > 0:
            sxA = sumAx / cntA
            syA = sumAy / cntA
            sxB = sumBx / cntB
            syB = sumBy / cntB
            d = sqrt((sxA - sxB) * (sxA - sxB) + (syA - syB) * (syA - syB))
            if d < best:
                best = d
        return best
    best = Solve(T, i + 1, sumAx + T[i][0], sumAy + T[i][1], cntA + 1, sumBx, sumBy, cntB, best)
    best = Solve(T, i + 1, sumAx, sumAy, cntA, sumBx + T[i][0], sumBy + T[i][1], cntB + 1, best)
    return best


def main() -> None:
    N = int(input())
    T = [[0.0, 0.0] for _ in range(N)]
    for i in range(N):
        s = input().split()
        T[i][0] = float(s[0])
        T[i][1] = float(s[1])
    print(Solve(T, 0, 0.0, 0.0, 0, 0.0, 0.0, 0, 999999999.0))


main()
