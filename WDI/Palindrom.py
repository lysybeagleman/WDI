def is_pal(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def solve():
    N = int(input())
    arr = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = input()
    dx = [1, -1,  0, 0,  1, 1, -1, -1]
    dy = [0,  0,  1,-1,  1,-1,  1, -1]
    found = ""
    for K in range(5, N + 1):
        count = 0
        for i in range(N):
            for j in range(N):
                for d in range(8):
                    x = i
                    y = j
                    s = ""
                    for _ in range(K):
                        if x < 0 or x >= N or y < 0 or y >= N:
                            break
                        s += arr[x][y]
                        x += dx[d]
                        y += dy[d]
                    if len(s) == K and is_pal(s):
                        count += 1
                        found = s
        if count == 2:
            print(found)
            return


solve()
