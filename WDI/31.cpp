#include<bits/stdc++.h>

using namespace std;

typedef long double ld;

ld f(ld x)
{
    return 1.0 / x;
}

void Solve()
{
    int n;
    ld k, s = 0.0, dx, x = 1;
    cin >> k;
    cin >> n;
    dx = (k - 1) / n;
    for (int i = 1;i <= n;++i)
    {
        x += dx;
        s += dx * f(x);
    }
    cout << "Field = " << s;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
