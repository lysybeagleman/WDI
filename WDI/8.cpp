#include<bits/stdc++.h>

using namespace std;

typedef long double ld;

const ld EPS = 0.00000001;

void Solve()
{

    ld x, n;
    cin >> n;
    x = n / 3.0;
    while (fabs(x * x * x - n) > EPS)
        x = (2.0 * x + n / (x * x)) / 3.0;
    cout << "Cuberoot " << n << " ≈ " << x;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
