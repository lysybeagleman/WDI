#include<bits/stdc++.h>

using namespace std;

bool Perfect(int n)
{
    int sum = 1, d;
    for (d = 2; d * d < n; ++d)
    {
        if (n % d == 0)
            sum += d + n / d;
    }
    if (d * d == n)
        sum += d;
    return ((sum == n) ? true : false);
}

void Solve()
{
    for (int i = 1; i < 1000000; ++i)
    {
        if (Perfect(i))
            cout << i << "\n";
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
