#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

void Solve()
{
    ll min_a = 0, min_b = 0, min_sum = LLONG_MAX, f1, f2, tmp;
    for (ll a = 2; a <= 2025; ++a)
    {
        for (ll b = 2; b <= 2025; ++b)
        {
            f1 = a, f2 = b;
            while (f2 <= 2025)
            {
                if (f2 == 2025)
                {
                    if (a + b < min_sum)
                    {
                        min_sum = a + b;
                        min_a = a;
                        min_b = b;
                    }
                    break;
                }
                tmp = f1 + f2;
                f1 = f2;
                f2 = tmp;
            }
        }
    }
    cout << "First = " << min_a << "\nSecond = " << min_b << "\n";
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
