#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

void Solve()
{
    ll n;
    cin >> n;
    bool flag = (n > 9);
    ld q = static_cast<ld>(((n / 10) % 10)) / static_cast<ld>((n % 10));
    n /= 10;
    while (n > 0 && flag)
    {
        if (static_cast<ld>(((n / 10) % 10)) / static_cast<ld>((n % 10)) != q)
            flag = false;
        q = static_cast<ld>(((n / 10) % 10)) / static_cast<ld>((n % 10));
        n /= 10;
    }
    cout << (flag ? "YES" : "NO");
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
