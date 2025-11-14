#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll N, res = 0, p = 5;
    cin >> N;
    while (p <= N)
    {
        res += N / p;
        p *= 5;
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
