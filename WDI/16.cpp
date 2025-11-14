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
    ll x, y, z;
    cin >> x;
    cin >> y;
    cin >> z;
    cout << "NWD = " << NWD(NWD(x, y), z);;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
