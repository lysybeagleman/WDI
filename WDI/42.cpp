#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll pow2_mod10(ll n)
{
    ll y = 1, p = 2;
    while (n > 0)
    {
        if (n % 2 == 1)
            y = (y * p) % 10;
        p = (p * p) % 10;
        n /= 2;
    }
    return y;
}

short g(short k)
{
    if (k <= 1)
        return 1;
    else if (k == 2)
        return 2;
    else if (k == 3)
        return 6;
    else
        return 4;
}

void Solve()
{
    ll N, res = 1;
    cin >> N;
    while (N > 0)
    {
        res = (res * g(N % 5) * pow2_mod10(N / 5)) % 10;
        N /= 5;
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
