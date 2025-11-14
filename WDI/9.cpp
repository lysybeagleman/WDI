#include<bits/stdc++.h>

using namespace std;

typedef long double ld;

const ld EPS = 0.0000001;

ld f(ld x)
{
    return pow(x, x) - 2024;
}

void Solve()
{
    ld a, b, x0, fa, fb, fx0;
    cin >> a;
    cin >> b;
    fa = f(a);
    fb = f(b);
    x0 = (a + b) / 2;
    fx0 = f(x0);
    if (fa * fb >= 0)
        cout << "Błąd: f(a) i f(b) muszą mieć różne znaki!";
    else
    {
        while (fabs(fx0) > EPS && fabs(b - a) > EPS)
        {
            if (fa * fx0 < 0)
                b = x0;
            else
            {
                a = x0;
                fa = fx0;
            }
            x0 = (a + b) / 2;
            fx0 = f(x0);
        }
        cout << "x = " << x0;
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
