#include<bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

void Solve()
{
    srand(time(NULL));
    ull N, max_len = 0, cur_len = 1;
    cin >> N;
    ull T[N];
    for (ull i = 0; i < N; ++i)
        T[i] = 1 + rand() % 18446744073709551615;
    for (ull m : T)
        cout << m << " ";
    cout << "\n";
    for (ull i = 1; i < N; ++i)
    {
        if (T[i] > T[i - 1])
        {
            ++cur_len;
            if (cur_len > max_len)
                max_len = cur_len;
        }
        else
            cur_len = 1;
    }
    cout << max_len;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
