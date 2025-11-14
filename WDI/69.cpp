#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

bool OddDigit(ll n)
{
    while (n > 0)
    {
        if ((n % 10) % 2 != 0)
            return true;
        n /= 10;
    }
    return false;
}

void Solve()
{
    bool flag = true;
    srand(time(NULL));
    ll n;
    cin >> n;
    ll T[n];
    for (ll i = 0; i < n; ++i)
        T[i] = 1 + rand() % 1000;
    for (ll k : T)
    {
        cout << k << " ";
        if (!OddDigit(k))
            flag = false;
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
