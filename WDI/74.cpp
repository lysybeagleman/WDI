#include<bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;
typedef long double ld;

void Solve()
{
    srand(time(NULL));
    ull N, max_len = 2, cur_len = 2;
    cin >> N;
    ull T[N];
    for (ull i = 0; i < N; ++i)
        T[i] = 1 + rand() % 50;
    for (ull m : T)
        cout << m << " ";
    cout << "\n";
    ld cur_q = T[1] / T[0];
    for (ull i = 2; i < N; ++i)
    {
        if (T[i] / T[i - 1] == cur_q)
        {
            ++cur_len;
            if (cur_len > max_len)
                max_len = cur_len;
        }
        else
        {
            cur_len = 2;
            cur_q = T[i] / T[i - 1];
        }
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
