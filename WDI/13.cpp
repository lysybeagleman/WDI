#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll n, d = 2;
    cin >> n;
    cout << n << " = ";
    while (d * d <= n)
    {
        if (n % d == 0)
        {
            cout << d << " * ";
            n /= d;
        }
        else
            ++d;
    }
    cout << n;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
