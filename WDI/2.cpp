#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    for (ll a = 1; a < 10; ++a)
    {
        for (ll b = 1; b < 10; ++b)
        {
            for (ll c = 1; c < 10; ++c)
            {
                if (3 * (100 * a + 10 * b + c) == 111 * b)
                    cout << "a = " << a << ", b = " << b << ", c = " << c << "\n";
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
