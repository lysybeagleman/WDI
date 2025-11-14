#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

bool IsFibo(ll x)
{
    ll t1 = 5*x*x + 4, t2 = 5*x*x - 4;
    ll s1 = static_cast<ll>(sqrt(t1)), s2 = static_cast<ll>(sqrt(t2));
    return (s1 * s1 == t1 || s2 * s2 == t2);
}

void Solve()
{
    bool flag = false;
    ll n, f1 = 1, f2 = 1, tmp;
    cin >> n;
    while (f1 <= n && !flag)
    {
        if (n % f1 == 0 && IsFibo(n / f1))
            flag = true;
        tmp = f2 + f1;
        f1 = f2;
        f2 = tmp;
    }
    cout << (flag ? "YES" : "NO");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
