#include<bits/stdc++.h>

using namespace std;

typedef long double ld;
const float EPS = 0.0000001;

void Solve()
{
    ld f1 = 1, f2 = 1, tmp, res = 0.0;
    while (fabs(f2 / f1 - res) > EPS)
    {
        res = f2 / f1;
        tmp = f2;
        f2 += f1;
        f1 = tmp;
    }
    cout << "Golden proportion: " << setprecision(7) << res;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
