#include<bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

bool Prime(ull n)
{
    if (n < 2)
        return false;
    if (n == 2 || n == 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
    for (ull d = 5; d * d <= n; d += 6)
    {
        if (n % d == 0 || n % (d + 2) == 0)
            return false;
    }
    return true;
}

void Solve()
{
    bool moved;
    srand(time(NULL));
    ull N, k = 0, n;
    cin >> N;
    ull T[N];
    for (ull i = 0; i < N; ++i)
        T[i] = 1 + rand() % 18446744073709551615;
    for (ull m : T)
        cout << m << " ";
    cout << "\n";
    while (k < N - 1)
    {
        moved = false;
        for (ull n = 2; n < T[k]; ++n)
        {
            if (T[k] % n == 0 && Prime(n))
            {
                k += n;
                moved = true;
                break;
            }
        }
        if (!moved)
            break;
    }
    cout << ((k == N - 1) ? "YES" : "NO");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
