#include<bits/stdc++.h>

using namespace std;

typedef long double ld;

void Solve()
{
    short N;
    cin >> N;
    ld res = 1.0;
    for (short i = 365; i >= 366 - N; --i)
        res *= static_cast<ld>(i) / 365.0;
    cout << 1.0 - res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
