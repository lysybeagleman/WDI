#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    bool flag = true;
    ll n;
    cin >> n;
    while (n > 0 && flag)
    {
        if ((n / 10) % 10 >= n % 10)
            flag = false;
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
