#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

bool TwoThreeFive(ll n)
{
    ll d = 2;
    while (d * d <= n)
    {
        if (n % d == 0)
        {
            if (d == 2 || d == 3 || d == 5)
                n /= d;
            else
                return false;
        }
        else
            ++d;
    }
    if (n == 2 || n == 3 || n == 5 || n == 1)
        return true;
    return false;
}

void Solve()
{
    ll N;
    cin >> N;
    cout << 1 << " ";
    for (ll i = 2; i <= N; ++i)
    {
        if (TwoThreeFive(i))
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
