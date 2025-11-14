#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    bool flag = false;
    ll f1 = 1, f2 = 1, tmp, n;
    cin >> n;
    while (f1 * f2 < n)
    {
        if (f1 * f2 == n)
            flag = true;
        tmp = f2;
        f2 += f1;
        f1 = tmp;
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
