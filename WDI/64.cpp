#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    string s = "";
    ll n;
    short d, p;
    cin >> n;
    cin >> p;
    while (n > 0)
    {
        d = n % p;
        s = static_cast<char>((d < 10) ? (d + 48) : (d + 55)) + s;
        n /= p;
    }
    cout << s;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
