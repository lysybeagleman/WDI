#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

short DigitSum(int n)
{
    short sum = 0;
    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

short FactorSum(int n)
{
    short sum = 0;
    int d = 2, check = n;
    while (d * d <= n)
    {
        if (n % d == 0)
        {
            sum += DigitSum(d);
            n /= d;
        }
        else
            ++d;
    }
    if (n != check)
        sum += DigitSum(n);
    return sum;
}

void Solve()
{
    for (int n = 2; n < 1000000; ++n)
    {
        if (DigitSum(n) == FactorSum(n))
            cout << n << " ";
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
