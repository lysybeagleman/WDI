#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll NWD(ll a, ll b)
{
    ll pom;
    while (b != 0)
    {
        pom = b;
        b = a % b;
        a = pom;
    }
    return a;
}

void Solve()
{
    ll x, y, z, nwd, nww;
    cin >> x;
    cin >> y;
    nwd = NWD(x, y);
    nww = x * y / nwd;
    cin >> z;
    nwd = NWD(nww, z);
    nww = nww * z / nwd;
    cout << "NWW = " << nww;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
