#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll N, c;
    cin >> N;
    for (ll a = 1; a < N - 1; ++a)
    {
        for (ll b = a; b < N - 1; ++b)
        {
            long double tmp = a * a + b * b;
            c = floor(sqrt(tmp));
            if (tmp == c * c)
            {
                cout << "a = " << a << ", b = " << b << ", c = " << c << "\n";
                cout << "b = " << a << ", a = " << b << ", c = " << c << "\n";
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
