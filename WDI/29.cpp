#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll n, curr_diff, min_diff, d = 1, a, b;
    cin >> n;
    min_diff = n;
    while (d * d <= n)
    {
        if (n % d == 0 && n / d - d < min_diff)
        {
            a = d;
            b = n / d;
            min_diff = n / d - d;
        }
        ++d;
    }
    cout << n << " = " << a << " * " << b;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
