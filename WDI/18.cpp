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
    ld x, cosx = 0;
    ll i = 0;
    cin >> x;
    while (!(x >= 0 && x <= 2 * M_PI))
    {
        if (x < 0)
            x += 2 * M_PI;
        if (x > 2 * M_PI)
            x -= 2 * M_PI;
    }
    while (pow(x, i) / Factorial(i) > EPS)
    {
        cosx += pow(-1, i / 2) * pow(x, i) / Factorial(i);
        i += 2;
    }
    cout << cosx;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
