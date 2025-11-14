#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll Length(ll n)
{
    ll l = 0;
    while (n > 0)
    {
        ++l;
        n /= 10;
    }
    return l;
}

void Solve()
{
    ll n, p, len, j, res = 0;
    cin >> n >> p;
    len = Length(n);
    ll T[pow(2, len) - 2];
    for (ll i = 0; i < pow(2, len) - 2; ++i)
    {
        num = 0;
        for (ll l = 1; l < len; ++l)
        {

        }
        T[i] = num;
    }
    for (ll n : T)
    {
        if (n % p == 0)
            ++res;
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
