#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll a, b, p, q, s;
    short n;
    cin >> a >> b >> n;
    s = a / b;
    cout << "a/b = " << s << ".";
    for (short i = 0; i < n; ++i)
    {
        p = (a % b) * 10;
        q = p / b;
        cout << q;
        a = p;
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
