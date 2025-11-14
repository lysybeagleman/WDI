#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const ld EPS = 0.0000001;

ll Factorial(ll n)
{
    ll factorial = 1;
    for (ll i = 2; i <= n; ++i)
        factorial *= i;
    return factorial;
}

void Solve()
{
    ll n = 0;
    ld e = 0.0;
    while (1.0 / Factorial(n) > EPS)
    {
        e += 1.0 / Factorial(n);
        ++n;
    }
    cout << "e ≈ " << e;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
