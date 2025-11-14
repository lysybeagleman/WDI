#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll Digits(ll n)
{
    ll sum = 1, d;
    for (d = 2; d * d < n; ++d)
    {
        if (n % d == 0)
            sum += d + n / d;
    }
    if (d * d == n)
        sum += d;
    return sum;
}

void Solve()
{
    for (ll i = 220; i < 1000000; ++i)
    {
        ll j = Digits(i);
        if (j > i && j < 1000000 && Digits(j) == i)
            cout << i << " " << j << "\n";
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
