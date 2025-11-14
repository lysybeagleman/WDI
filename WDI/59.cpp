#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll QuickExponentiating(ll x, ll n)
{
    ll tmp = x, y = 1;
    while (n > 0)
    {
        if (n % 2 == 1)
            y *= tmp;
        n /= 2;
        if (n > 0)
            tmp *= tmp;
    }
    return y;
}

ll DigitSum(ll n, ll D[])
{
    ll sum = 0;
    while (n > 0)
    {
        sum += D[n % 10];
        n /= 10;
    }
    return sum;
}

void Solve()
{
    ll N, start;
    ll D[10];
    cin >> N;
    start = QuickExponentiating(10, N - 1);
    for (short i = 0; i < 10; ++i)
        D[i] = QuickExponentiating(i, N);
    for (ll i = start; i < start * 10; ++i)
    {
        if (i == DigitSum(i, D))
            cout << i << " ";
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
