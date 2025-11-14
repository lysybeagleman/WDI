#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const float EPS = 0.0000000001;

void Solve()
{
    ld a, b, fx, fprimx;
    cin >> a;
    cin >> b;
    ld x = (a + b) / 2.0;
    ld xn = x + 2 * EPS;
    while (fabsl(xn - x) > EPS)
    {
        x = xn;
        fx = pow(x, x) - 2020.0;
        fprimx = pow(x, x) * (log(x) + 1);
        xn = x - fx / fprimx;
    }
    cout << setprecision(12) << x;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
