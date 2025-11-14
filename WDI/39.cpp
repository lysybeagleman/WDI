#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;
    while (e != 0)
    {
        if ((a + b + d + e) / 4 == c)
            cout << c << " ";
        a = b;
        b = c;
        c = d;
        d = e;
        cin >> e;
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
