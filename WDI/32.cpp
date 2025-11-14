#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    bool flag = false;
    ll k, a = 2;
    cin >> k;
    while (a <= k)
    {
        if (k % a == 0)
            flag = true;
        cout << a << " ";
        a = 3 * a + 1;
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
