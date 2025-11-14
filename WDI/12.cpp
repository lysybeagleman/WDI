#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    int n, d;
    cin >> n;
    cout << 1 << " ";
    for (d = 2; d * d < n; ++d)
    {
        if (n % d == 0)
            cout << d << " " << n / d << " ";
    }
    if (d * d == n)
        cout << d << " ";
    cout << n;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
