#include<bits/stdc++.h>

using namespace std;

const double EPS = 0.0000001;

float Calculate(short n)
{
    if (n == 1)
        return sqrt(0.5);
    return sqrt(0.5 + 0.5 * Calculate(n - 1));
}

void Solve()
{
    float prod = sqrt(0.5);
    short n = 2;
    while (fabs(Calculate(n) - Calculate(n - 1)) > EPS)
    {
        prod *= Calculate(n);
        ++n;
    }
    cout << "π ≈ " << 2.0 / prod;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    Solve();
    return 0;
}
