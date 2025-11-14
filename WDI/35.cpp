#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    bool flag = false;
    ll n, tmp, counter = 0;
    cin >> n;
    tmp = n;
    while (tmp > 0)
    {
        ++counter;
        tmp /= 10;
    }
    while (n > 0 && !flag)
    {
        if (n % 10 == counter)
            flag = true;
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
