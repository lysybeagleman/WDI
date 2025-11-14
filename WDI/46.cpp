#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

void Solve()
{
    ll m, n, res = 0;
    cin >> m >> n;
    ld sq = sqrt(m);
    for (ll i = 0; i < n; ++i)
    {
        sq -= floor(sq);
        sq *= 10;
        res += ll(sq);
    }
    cout << res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
