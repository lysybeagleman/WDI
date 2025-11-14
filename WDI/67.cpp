#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

void Solve()
{
    ld e = 1.0, factorial = 1;
    short N;
    cin >> N;
    const ld EPS = pow(0.1, N);
    for (ll n = 1; 1.0 / factorial > EPS; ++n)
    {
        factorial *= n;
        e += 1.0 / factorial;
    }
    cout << setprecision(N) << e;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
